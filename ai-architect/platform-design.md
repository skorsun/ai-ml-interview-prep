# Platform Design

## Question
Design an enterprise AI platform.

### High-Level Diagram

Data Sources
   |
   v
Data Platform
   |
   v
Feature / Context Layer
   |
   v
Model Registry
   |
   v
Serving Layer
   |
   v
Products / APIs

### Great answer
I separate data, models, and serving
to allow independent evolution and ownership.