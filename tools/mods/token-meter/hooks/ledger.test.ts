import { expect, test } from 'claude-code/testing'

import type { Finished } from '../types'
import { appendRows, cacheHitPercent, effortOf, ledgerRow, runNumber, stageNumber, wall } from './ledger'

const f: Finished = {
  key: 'a:1', agentId: 'a', type: 'stage-05-concall', description: 'concall analysis',
  model: 'claude-sonnet-5-5', tokens: { input: 1000, output: 2000, cacheRead: 9000, cacheWrite: 0 },
  wallMs: 125_000, logged: false,
}

test('stage numbers follow the ledger convention', () => {
  expect(stageNumber('stage-05-concall')).toBe('5')
  expect(stageNumber('stage-09b-dossier')).toBe('09b')
  expect(stageNumber('verifier-a-numerical')).toBe('12a')
  expect(stageNumber('quarterly-a3-forensics')).toBe('A3')
  expect(stageNumber('general-purpose')).toBe('-')
})

test('cache hit rate is cache reads over all input', () => {
  expect(cacheHitPercent(f.tokens)).toBe(90)
  expect(cacheHitPercent({ input: 0, output: 5, cacheRead: 0, cacheWrite: 0 })).toBe(null)
})

test('effort comes from agent frontmatter', () => {
  expect(effortOf('---\nname: x\nmodel: claude-opus-5-5\neffort: high\n---\nbody')).toBe('high')
  expect(effortOf('---\nname: x\n---\neffort: low')).toBe('default')
  expect(effortOf(null)).toBe('default')
})

test('a row matches the ledger shape and run# counts prior rows', () => {
  const ledger = '| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |\n|---|\n| 5 | concall | sonnet | default | - | - | 155072 | 8m17s | 1 |\n'
  const run = runNumber(ledger, '5', 'x')
  expect(run).toBe(2)
  expect(ledgerRow(f, 'default', run)).toBe(
    '| 5 | concall analysis (stage-05-concall) | claude-sonnet-5-5 | default | 10000 | 2000 | 12000 | 2m05s | 2 |',
  )
  expect(wall(59_400)).toBe('0m59s')
})

test('append adds the header to a new ledger and keeps old text', () => {
  const fresh = appendRows(null, 'abc-2026-10-03', ['| 1 | x |'])
  expect(fresh.startsWith('# SESSION COST LEDGER — abc-2026-10-03')).toBe(true)
  expect(fresh.includes('| # | stage | model | effort | in_tok | out_tok | total_tok | wall | run# |')).toBe(true)
  const old = '# L\n\n| # | stage | model |\n|---|\n| 1 | a |\n'
  expect(appendRows(old, 't', ['| 2 | b |'])).toBe(`${old}| 2 | b |\n`)
})
