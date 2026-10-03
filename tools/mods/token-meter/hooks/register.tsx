import { atom, read, update } from 'claude-code'
import type { Register } from 'claude-code'

import type { Finished, Running, Tokens } from '../types'
import {
  PIPELINE_AGENT, ZERO, add, appendRows, cacheHitPercent, effortOf, ledgerRow,
  runNumber, short, stageLabel, stageNumber, totalTokens,
} from './ledger'

const session = atom({ plugin: 'token-meter', key: 'session' } as const, ZERO)
const running = atom({ plugin: 'token-meter', key: 'running' } as const, [] as Running[])
const finished = atom({ plugin: 'token-meter', key: 'finished' } as const, [] as Finished[])
const isHidden = atom({ plugin: 'token-meter', key: 'isHidden' } as const, false)

const USAGE = 'Usage: /stage-cost runs/<ticker>-<date> [--all]. Appends one line per finished stage to that folder\'s session-cost.md.'

export const register: Register = on => {
  on('session.start', async ($, e, next) => {
    await $.command.register({ name: 'cost-bar', description: 'Show or hide the token band above the prompt' })
    await $.command.register({
      name: 'stage-cost',
      description: 'Append one session-cost.md line per finished pipeline stage: /stage-cost runs/<folder> [--all]',
    })
    return next(e)
  })

  on('agent.spawn', async ($, e, next) => {
    const started = await next(e)
    if ('agentId' in started && started.agentId) {
      const entry: Running = {
        agentId: started.agentId,
        type: e.subagentType,
        description: e.description,
        startedAt: await $.clock.now(),
      }
      await update($, running, list => [...list.filter(r => r.agentId !== entry.agentId), entry])
    }
    return started
  })

  on('turn.complete', async ($, e, next) => {
    const result = await next(e)
    const usage = e.usage
    if (!usage) return result
    const tokens: Tokens = {
      input: usage.input_tokens,
      output: usage.output_tokens,
      cacheRead: usage.cache_read_input_tokens,
      cacheWrite: usage.cache_creation_input_tokens,
    }
    await update($, session, total => add(total, tokens))
    if (!e.agentId) return result

    const now = await $.clock.now()
    const list = await read($, running)
    const run = list.find(r => r.agentId === e.agentId)
    const done: Finished = {
      key: `${e.agentId}:${now}`,
      agentId: e.agentId,
      type: run?.type ?? 'subagent',
      description: run?.description ?? e.agentId,
      model: usage.model,
      tokens,
      wallMs: run ? now - run.startedAt : 0,
      logged: false,
    }
    // A continued agent (SendMessage) times its next run from this completion.
    await update($, running, rs => rs.map(r => (r.agentId === e.agentId ? { ...r, startedAt: now } : r)))
    await update($, finished, fs => [...fs, done].slice(-200))
    return result
  })

  on('command.run', { command: 'cost-bar' }, async $ => {
    const hidden = await update($, isHidden, h => !h)
    return { text: hidden ? 'Token band hidden. /cost-bar shows it again.' : 'Token band shown.' }
  })

  on('command.run', { command: 'stage-cost' }, async ($, e) => {
    const parts = e.args.trim().split(/\s+/).filter(Boolean)
    const folder = parts.find(p => !p.startsWith('--'))?.replace(/\/+$/, '')
    const includeAll = parts.includes('--all')
    if (!folder) return { text: USAGE }
    if (!(await $.fs.exists(folder))) return { text: `No folder ${folder}. ${USAGE}` }

    const pending = (await read($, finished)).filter(f => !f.logged && (includeAll || PIPELINE_AGENT.test(f.type)))
    if (pending.length === 0) return { text: 'No finished stages waiting. Nothing appended.' }

    const path = `${folder}/session-cost.md`
    let ledger: string | null = (await $.fs.exists(path)) ? await $.fs.read(path) : null
    const rows: string[] = []
    for (const f of pending) {
      const agentPath = `.claude/agents/${f.type}.md`
      const agentFile = (await $.fs.exists(agentPath)) ? await $.fs.read(agentPath) : null
      const stage = stageNumber(f.type)
      const run = runNumber(`${ledger ?? ''}\n${rows.join('\n')}`, stage, stageLabel(f))
      rows.push(ledgerRow(f, effortOf(agentFile), run))
    }
    ledger = appendRows(ledger, folder.split('/').pop() ?? folder, rows)
    await $.fs.write(path, ledger)

    const keys = new Set(pending.map(f => f.key))
    await update($, finished, fs => fs.map(f => (keys.has(f.key) ? { ...f, logged: true } : f)))
    return { text: `Appended ${rows.length} line(s) to ${path}:\n${rows.join('\n')}` }
  })

  on('ui.render', { component: 'AbovePrompt' }, async ($, e, next) => {
    const total = await read($, session)
    if (e.props.hasSurvey || (await read($, isHidden)) || totalTokens(total) === 0) return next(e)

    const { Box, Text } = $.ui.resolve(e)
    const done = await read($, finished)
    const hit = cacheHitPercent(total)
    const recent = done.slice(-3).reverse()
    const waiting = done.filter(f => !f.logged && PIPELINE_AGENT.test(f.type)).length

    return (
      <Box flexDirection="column">
        <Text dimColor>
          tokens {short(totalTokens(total))} · cache hit {hit === null ? 'n/a' : `${hit}%`} · subagents done {done.length}
          {waiting > 0 ? ` · ${waiting} stage line(s) for /stage-cost` : ''}
        </Text>
        {recent.length > 0 && (
          <Text dimColor>
            last: {recent.map(f => `${f.type} ${short(totalTokens(f.tokens))}`).join(' | ')}
          </Text>
        )}
      </Box>
    )
  })
}
