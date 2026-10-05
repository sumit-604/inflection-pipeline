import { expect, mock, test } from 'claude-code/testing'

const PROPS = { hasSurvey: false, isWorking: false, maxRows: 3, bodyColumns: 100 } as never

test('a finished stage shows in the band and /stage-cost appends one ledger line', async ($, on) => {
  const clock = mock.clock(on, { now: 1_000_000 } as never)
  const files: Record<string, string> = {
    'runs/demo-2026-10-03/manifest.yaml': 'ticker: DEMO\n',
    '.claude/agents/stage-05-concall.md': '---\nname: stage-05-concall\nmodel: claude-sonnet-5-5\neffort: medium\n---\nbody\n',
    'runs/demo-2026-10-03/session-cost.md':
      '# SESSION COST LEDGER — DEMO\n\n| # | stage | model | effort | in_tok | cache_read | cache_write | out_tok | total_tok | wall | run# |\n|---|---|---|---|---|---|---|---|---|---|---|\n| 1 | gate 0 | sonnet | default | - | - | - | - | 134317 | 10m07s | 1 |\n',
  }
  const key = (path: string) => Object.keys(files).find(k => path === k || path.endsWith(`/${k}`)) ?? path
  const seen: string[] = []
  on('agent.spawn', (_$, _e) => ({ model: 'claude-sonnet-5-5', agentId: 'ag1' }) as never)
  on('turn.complete', (_$, e) => ({ text: e.answer, usage: e.usage }))
  on('fs.exists', (_$, e) => (seen.push(e.path), { value: key(e.path) in files || /runs\/demo-2026-10-03$/.test(e.path) }))
  on('fs.read', (_$, e) => {
    const text = files[key(e.path)]
    if (text === undefined) throw new Error(`missing ${e.path}`)
    return { value: text }
  })
  on('fs.write', (_$, e) => {
    files[key(e.path)] = e.text
    return { value: undefined }
  })

  await $.agent.spawn({
    tool_use_id: 't1', prompt: 'run stage 5', description: 'concall analysis', subagentType: 'stage-05-concall',
    provider: { plugin: 'engine', tier: 'core' }, parentModel: 'claude-opus-5-5', background: false, fork: false,
  } as never)
  await clock.advance(125_000)
  await $.turn.complete({
    reason: 'answer', answer: 'done', durationMs: 125_000, isAborted: false, turnId: 'tu1', agentId: 'ag1',
    usage: { model: 'claude-sonnet-5-5', input_tokens: 1_000, output_tokens: 2_000, cache_read_input_tokens: 9_000, cache_creation_input_tokens: 0 },
  } as never)

  for (const surface of ['terminal', 'desktop'] as const) {
    const ui = await $.ui.mount({ plugin: 'token-meter', surface, component: 'AbovePrompt', props: PROPS })
    expect(await ui.find({ type: 'Text', text: /tokens 12k · cache hit 90% · subagents done 1 · 1 stage line/ })).toBeDefined()
    expect(await ui.find({ type: 'Text', text: /last: stage-05-concall 12k/ })).toBeDefined()
    await ui.unmount()
  }

  const r = await $.command.run({ command: 'stage-cost', args: 'runs/demo-2026-10-03' } as never)
  expect([(r as { text: string }).text, seen.join(',')].join(' | ')).toContain('Appended 1 line(s)')
  expect(files['runs/demo-2026-10-03/session-cost.md']).toContain(
    '| 1 | gate 0 | sonnet | default | - | - | - | - | 134317 | 10m07s | 1 |\n| 5 | concall analysis (stage-05-concall) | claude-sonnet-5-5 | medium | 10000 | 9000 | 0 | 2000 | 12000 | 2m05s | 1 |\n',
  )

  const again = await $.command.run({ command: 'stage-cost', args: 'runs/demo-2026-10-03' } as never)
  expect((again as { text: string }).text).toContain('Nothing appended')

  const toggled = await $.command.run({ command: 'cost-bar', args: '' } as never)
  expect((toggled as { text: string }).text).toContain('hidden')
})
