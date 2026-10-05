import type { Finished, Tokens } from '../types'

export const ZERO: Tokens = { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 }

export const LEDGER_HEADER = [
  '| # | stage | model | effort | in_tok | cache_read | cache_write | out_tok | total_tok | wall | run# |',
  '|---|-------|-------|--------|--------|------------|-------------|---------|-----------|------|------|',
]

export const PIPELINE_AGENT = /^(stage-|verifier-|quarterly-)/

// Every input token the call was answered over: uncached, cache-read and cache-written.
export const inTokens = (t: Tokens): number => t.input + t.cacheRead + t.cacheWrite

export const totalTokens = (t: Tokens): number => inTokens(t) + t.output

export const add = (a: Tokens, b: Tokens): Tokens => ({
  input: a.input + b.input,
  output: a.output + b.output,
  cacheRead: a.cacheRead + b.cacheRead,
  cacheWrite: a.cacheWrite + b.cacheWrite,
})

// Share of input tokens served from the prompt cache, 0-100; null before any input.
export const cacheHitPercent = (t: Tokens): number | null => {
  const all = inTokens(t)
  return all === 0 ? null : Math.round((t.cacheRead / all) * 100)
}

export const short = (n: number): string =>
  n >= 1_000_000 ? `${(n / 1_000_000).toFixed(2)}M` : n >= 1_000 ? `${Math.round(n / 1_000)}k` : String(n)

// The ledger's "#" column: stage-05-concall -> 5, stage-09b-dossier -> 09b,
// verifier-a-numerical -> 12a, quarterly-a1-extractor -> A1, anything else -> "-".
export const stageNumber = (type: string): string => {
  const stage = /^stage-(\d+)([a-z]?)-/.exec(type)
  if (stage) return stage[2] ? `${stage[1]}${stage[2]}` : String(Number(stage[1]))
  const verifier = /^verifier-([a-d])-/.exec(type)
  if (verifier) return `12${verifier[1]}`
  const quarterly = /^quarterly-(a\d)-/.exec(type)
  if (quarterly?.[1]) return quarterly[1].toUpperCase()
  return '-'
}

export const wall = (ms: number): string => {
  const s = Math.max(0, Math.round(ms / 1000))
  return `${Math.floor(s / 60)}m${String(s % 60).padStart(2, '0')}s`
}

// The agent file's `effort:` frontmatter value, or "default" when it sets none.
export const effortOf = (agentFile: string | null): string => {
  if (!agentFile) return 'default'
  const front = /^---\n([\s\S]*?)\n---/.exec(agentFile)?.[1]
  const effort = front === undefined ? undefined : /^effort:\s*(\S+)/m.exec(front)?.[1]
  return effort ?? 'default'
}

// run# = how many rows for the same stage label the ledger already holds, plus one.
// Counts both row shapes: the 9-column rows of older ledgers (11 cells after the
// split on '|') and the current 11-column rows (13 cells). # and stage sit in
// cells 1 and 2 in both.
export const runNumber = (ledger: string, stage: string, stageName: string): number => {
  let n = 0
  for (const line of ledger.split('\n')) {
    const cells = line.split('|').map(c => c.trim())
    if (cells.length < 11) continue
    if (stage !== '-' ? cells[1] === stage : cells[2] === stageName) n += 1
  }
  return n + 1
}

export const stageLabel = (f: Finished): string => `${f.description} (${f.type})`.replace(/\|/g, '/')

export const ledgerRow = (f: Finished, effort: string, run: number): string => {
  const t = f.tokens
  return `| ${stageNumber(f.type)} | ${stageLabel(f)} | ${f.model} | ${effort} | ${inTokens(t)} | ${t.cacheRead} | ${t.cacheWrite} | ${t.output} | ${totalTokens(t)} | ${wall(f.wallMs)} | ${run} |`
}

// Appends rows to a ledger's text, adding the current header when the ledger is new or
// has none. A ledger that holds only the older 9-column header gets the current header
// as a new table below its old text, so wide rows never sit under a narrow header.
export const appendRows = (ledger: string | null, title: string, rows: string[]): string => {
  let text = ledger ?? `# SESSION COST LEDGER — ${title}\n\n`
  if (!text.includes(LEDGER_HEADER[0] as string)) text = `${text.replace(/\n*$/, '\n\n')}${LEDGER_HEADER.join('\n')}\n`
  return `${text.replace(/\n*$/, '\n')}${rows.join('\n')}\n`
}
