# LLM System Design

## Question
Design an LLM-powered customer support assistant.

### What interviewers are testing
- system thinking
- reliability awareness
- ability to ship AI, not demo it

### Great answer
I start with the user goal, then design:
- context retrieval (what data, why)
- prompt structure
- evaluation signals
- fallbacks for failure cases

The LLM is treated as a component inside a larger system,
not the system itself.

# LLM System Design

## Question
Design an LLM-powered assistant.

### LLM System Diagram

User
  |
  v
API Gateway
  |
  v
Context Builder
  |---> Vector DB (retrieval)
  |---> User State / Memory
  |
  v
Prompt Template
  |
  v
LLM Inference
  |
  v
Post-Processing
  |---> Safety Filters
  |---> Output Validation
  |
  v
Response to User

### Great answer
I design the system around failure modes.
The LLM is treated as a probabilistic component,
with guardrails, fallbacks, and monitoring.

## 2. Visual Diagrams (GitHub-Renderable → PNG/SVG)

### Option A: Mermaid Diagram (GitHub auto-renders)

```mermaid
flowchart TB
    User --> API
    API --> Context
    Context --> VectorDB
    Context --> Prompt
    Prompt --> LLM
    LLM --> Safety
    Safety --> Response
````

### Option B: ASCII Diagram (Interview-Friendly)

```text
User
  |
API Gateway
  |
Context Builder
  |----> Vector DB (RAG)
  |
Prompt Template
  |
LLM
  |
Safety + Validation
  |
Response
````

Interviewers *love* candidates who can draw this cleanly.