# Drill 2: Internal Analytics Copilot

## Prompt
Design an LLM that helps managers query internal data safely.

## Constraints
- Sensitive data
- No SQL hallucinations
- Auditable outputs

## Interviewer is testing
- permission boundaries
- tool calling design
- blast-radius control

## Strong answer outline
- Schema-aware query generation
- Read-only execution layer
- Result summarization separate from querying
- Logging and traceability

## Red flag
Letting the LLM directly execute queries.