# Data & Feature Engineering

## Question
How do you decide which features to engineer first?

### What interviewers are looking for
- prioritization
- signal vs noise thinking
- production awareness

### Great answer
I start from the target metric and identify raw signals most directly related to it.
I prioritize features that are:
- available at serving time
- stable over time
- cheap to compute

I usually build simple versions first and validate impact with ablation
before investing in complex transformations.