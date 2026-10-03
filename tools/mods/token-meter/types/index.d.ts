export type Tokens = {
  input: number
  output: number
  cacheRead: number
  cacheWrite: number
}

export type Running = {
  agentId: string
  type: string
  description: string
  startedAt: number
}

export type Finished = {
  key: string
  agentId: string
  type: string
  description: string
  model: string
  tokens: Tokens
  wallMs: number
  logged: boolean
}

declare module 'claude-code' {
  interface PluginState {
    'token-meter': {
      session: Tokens
      running: Running[]
      finished: Finished[]
      isHidden: boolean
    }
  }
}
