# My AI Engineering Path
<!-- Managed by the ai-engineering-from-scratch learning skills.
     Repo: https://github.com/rohitg00/ai-engineering-from-scratch -->

## Mission

I want a solid foundation for an **Agent Engineer / Software Engineer (Agent)
new-grad 2027** role — the Sierra "Agent Engineering New Grad" class of job in
London, and the equivalent at OpenAI and Anthropic. Those roles are about
shipping production-grade AI agents: owning the agent development life cycle
from pilot to deployment, tuning agents that run in production for enterprise
customers, and building agent frameworks and tooling. The job description
specifically names eval frameworks, agent tooling, RAG pipelines, and prompt
engineering as the relevant skills.

By the end I most want to be able to build **an autonomous agent** — a
tool-using agent loop I wrote myself and fully understand, not a framework
wrapper.

Working note on how to teach me: my theory is strong (10/10 on placement) but
I am a coding beginner, so the bottleneck is implementation, not concepts. I
learn by typing code, not by reading finished solutions. Python is the
language for every lesson that offers a choice.

## Placement

- Date: 2026-11-05
- Score: 10/10 — Math & Statistics 2/2, Classical ML 2/2, Deep Learning 2/2,
  NLP & Transformers 2/2, Applied AI 2/2
- Entry point: Phase 14: Agent Engineering
- Pace: as fast as possible (no weekly cap)

## Path

| Phase | Name | Status | Est. hours |
|-------|------|--------|------------|
| 0 | Setup & Tooling | Skip | -- |
| 1 | Math Foundations | Skip | -- |
| 2 | ML Fundamentals | Skip | -- |
| 3 | Deep Learning Core | Skip | -- |
| 4 | Computer Vision | Skip | -- |
| 5 | NLP — Foundations to Advanced | Skip | -- |
| 6 | Speech & Audio | Skip | -- |
| 7 | Transformers Deep Dive | Skip | -- |
| 8 | Generative AI | Skip | -- |
| 9 | Reinforcement Learning | Skip | -- |
| 10 | LLMs from Scratch | Skip | -- |
| 11 | LLM Engineering | Skip | -- |
| 12 | Multimodal AI | Skip | -- |
| 13 | Tools & Protocols | Skip | -- |
| 14 | Agent Engineering | Do | 55 |
| 15 | Autonomous Systems | Do | 20 |
| 16 | Multi-Agent & Swarms | Do | 28 |
| 17 | Infrastructure & Production | Do | 34 |
| 18 | Ethics, Safety & Alignment | Do | 31 |
| 19 | Capstone Projects | Do | 620 |

Path total: ~788 hours across 6 phases.

### Recommended additions beyond the score

The placement score alone marks everything below Phase 14 as Skip. Two of
those phases are worth pulling in anyway, for reasons the quiz cannot see:

- **Phase 13: Tools & Protocols (~76 h)** — tool calling, function schemas,
  and MCP are the substrate every Phase 14 lesson sits on, and the target job
  description names agent tooling directly. Strong candidate to interleave
  with Phase 14 rather than skip.
- **Phase 11: LLM Engineering (~19 h)** — evals, prompting, and RAG
  pipelines, all named in the job description.

The quiz measured concept recognition, which is my strength. It did not
measure whether I can write the code. If a Phase 14 lesson's Build It section
feels like it is testing Python rather than agent design, that is the real gap
and the fix is more typing, not an earlier phase.

## Progress log

| Date | Lesson | Quiz | Note |
|------|--------|------|------|
| 2026-11-07 | 14/01 the-agent-loop | 2/2 | Typed the full loop in `scratch/agent_loop.py`; trace matches reference. Also did Exercise 3 (malformed reply becomes an error observation). Recurring slips: `print` vs `return`, unclosed brackets, `self = {}` vs `self.x = {}`, using a variable inside the `except` that failed to exist. |
| 2026-11-07 | 14/02 rewoo-plan-and-execute | 1/2 | Built `scratch/rewoo.py` reusing own `ToolRegistry`; output matches reference. Found and fixed the `#E1`-inside-`#E10` bug (longest key first). Got stuck on data flow in `run_workers` until shown a per-step state table. Missed Plan-and-Act (not covered in depth while teaching). |

## Review queue

<!-- learn adds lessons the quizzes flag -->
- 14/02 rewoo-plan-and-execute: Plan-and-Act — long-horizon (>30 step) web/mobile tasks, planner trained on synthetic plans; when to pick it over plain ReWOO.
