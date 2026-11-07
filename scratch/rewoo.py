from __future__ import annotations
from dataclasses import dataclass
from agent_loop import ToolRegistry

@dataclass
class PlanStep:
    id: str
    tool: str
    args: dict

@dataclass
class Plan:
    steps: list

def resolve(value, evidence):
    if not isinstance(value,str):
        return value
    for key in sorted(evidence,key=len, reverse=True):
        value = value.replace(f'#{key}', evidence[key])
    return value

def run_workers(plan, tools):
    evidence = {}
    for step in plan.steps:
        new_args = {}
        for key,value in step.args.items():
            new_args[key] = resolve(value,evidence)
        unresolved = False
        for key in new_args:
            if isinstance(new_args[key],str) and '#E' in new_args[key] :
                unresolved = True
        if unresolved:
            evidence[step.id] = f"error: step {step.id} refers to evidence that doesn't exist yet"
        else:
            evidence[step.id] =tools.dispatch(step.tool, new_args)
    return evidence

class ScriptedPlanner:
    def __init__(self, plan):
        self.plan = plan
    def plan_for(self, question):
        return self.plan

class ScriptedSolver:
    def __init__(self, template):
        self.template = template
    def solve(self, question, plan, evidence):
        return self.template.format(**evidence)

def search(query):
    if query.lower() == "capital of france":
        return 'Paris'
    elif query.lower() == 'population of paris':
        return '11.2 million metro'
    else:
        return f"no result for '{query}'"

def round_million(text):
    words = text.split()
    rounded = round(float(words[0]))
    return f'{rounded} million'

def main():
    tools = ToolRegistry()
    tools.register('search', search)
    tools.register('round_million',round_million)
    plan = Plan(steps=[
        PlanStep("E1", "search",        {"query": "capital of France"}),
        PlanStep("E2", "search",        {"query": "population of #E1"}),
        PlanStep("E3", "round_million", {"text": "#E2"}),
    ])
    planner = ScriptedPlanner(plan)
    solver = ScriptedSolver("The capital of France is {E1}; rounded population is {E3}.")
    question = "what's the population of capital of france?"
    plan     = planner.plan_for(question)
    print(f'PLAN : ')
    for step in plan.steps:
        print (f" {step.id}: {step.tool}({step.args})")
    evidence = run_workers(plan, tools)
    print(f'EVIDENCE : ')
    for key, result in evidence.items():
        print(f"{key} -> {result}")
    answer   = solver.solve(question, plan, evidence)
    print(f"FINAL : {answer}")
    
if __name__ == '__main__':
    main()
        