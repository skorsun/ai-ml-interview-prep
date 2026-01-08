# Training & Evaluation

## Question
How do you choose an evaluation metric?

### What interviewers are testing
- alignment with business goals
- awareness of trade-offs
- avoidance of proxy metrics

### Great answer
I start from the cost of different error types.
If false positives and false negatives have different business impact,
accuracy is usually the wrong metric.

I choose:
- one primary metric for optimization
- secondary metrics as guardrails

This prevents over-optimizing the wrong behavior.