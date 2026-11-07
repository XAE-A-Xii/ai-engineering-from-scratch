from __future__ import annotations
from dataclasses import dataclass

class ToolRegistry:
    def __init__(self):
        self._tools = {}
    def register(self, name, fn):
        self._tools[name] = fn
    def names(self):
        return sorted(self._tools)
    def dispatch(self, name, args):
        fn = self._tools.get(name)
        if fn is None:
            return f'error: Unknown tool: {name}'
        try:
            return fn(**args)
        except TypeError as e:
            return f'error: {e}'
        except Exception as e:
            return f'error: {type(e).__name__} : {e}'

@dataclass
class ToolCall:
    name: str
    args: dict

@dataclass
class Turn:
    kind: str
    content: str
    tool_call: ToolCall | None = None
    observation: str | None = None

class ToyLLM:
    def __init__(self, script):
        self.script = script
        self.cursor = 0
    def respond(self, history):
        if (self.cursor >= len(self.script)):
            return {'kind': 'finish', 'content':'no more actions'}
        to_be_returned = self.script[self.cursor]
        self.cursor += 1
        return to_be_returned

def calculator(expr):
    allowed = '0123456789+-*/(). '
    used = set(expr)
    if used.issubset(allowed):
        try:
            ans = eval(expr, {"__builtins__":{}}, {})
        except Exception as e:
            return f'error: {type(e).__name__} : {e}'
        return str(ans)
    return 'error: expression contained characters that aren’t allowed.'

class KVStore:
    def __init__(self):
        self._store = {}
    def set(self, key, value):
        self._store[key] = value
        return f'stored {key}'
    def get(self, key):
        return self._store.get(key, f'missing {key}')

class AgentLoop:
    def __init__(self, llm, tools, max_turns=12):
        self.llm = llm
        self.tools = tools
        self.max_turns = max_turns
        self.history = []

    def run(self, user_message):
        self.history.append(Turn('user',user_message))
        for i in range(self.max_turns):
            answer = self.llm.respond(self.history)
            if answer['kind'] == 'finish':
                self.history.append(Turn('final', answer['content']))
                return answer['content']
            self.history.append(Turn('thought', answer.get("thought", "")))
            try:
                call = ToolCall(answer['action'], answer.get("args", {}))
                observation = self.tools.dispatch(call.name, call.args)
                self.history.append(Turn('action',call.name,tool_call=call,observation=observation))
            except KeyError as e:
                observation = "error: reply had no 'action' key"
                self.history.append(Turn('action','<missing>',tool_call=ToolCall('<missing>', {}),observation=observation))
                
        self.history.append(Turn('final', 'budget exhausted'))
        return 'budget exhausted'

def pretty_trace(history):
    for i, turn in enumerate(history):
        if turn.kind == 'action':
            print(f'[{i:02d} {turn.kind:>7}] {turn.content}({turn.tool_call.args}) -> {turn.observation}')
        else:
            print(f'[{i:02d} {turn.kind:>7}] {turn.content}')

def main():
    tools = ToolRegistry()
    kv = KVStore()
    tools.register('calculator', calculator)
    tools.register('kv_set', kv.set)
    tools.register('kv_get',kv.get)
    script = [{"kind": "action", "thought": "store the base price", "action": "kv_set", "args": {"key": "base", "value": "120"}},
    {"kind": "action", "thought": "compute 15% tax", "action": "calculator", "args": {"expr": "120 * 0.15"}},
    {"kind": "action", "thought": "store the tax", "action": "kv_set", "args": {"key": "tax", "value": "18.0"}},
    {"kind": "action", "thought": "compute the total", "action": "calculator", "args": {"expr": "120 + 18.0"}},
    {"kind": "action", "thought": "read base back to confirm it", "action": "kv_get", "args": {"key": "base"}},
    {"kind": "finish", "content": "final answer is 138"}]
    loop = AgentLoop(ToyLLM(script), tools, 10)
    answer = loop.run('Calculate the tax addition on base 120 ?')
    pretty_trace(loop.history)
    print(answer)

if __name__ == "__main__":
    main()
            

    
                
        
    
    
    