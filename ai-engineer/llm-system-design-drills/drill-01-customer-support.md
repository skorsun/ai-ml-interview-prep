# Drill 1: LLM-Powered Customer Support Agent

## Prompt
Design an LLM-powered customer support assistant for a SaaS product.

## Constraints
- Must respond under 2 seconds
- Must not hallucinate policies
- Must support 100k daily users
- Cost matters

## Interviewer is testing
- system decomposition
- RAG correctness
- latency vs cost trade-offs
- safety thinking

## Strong answer outline
1. User intent classification
2. Retrieval from a trusted knowledge base
3. Prompt grounded only in retrieved context
4. Output validation against policy constraints
5. Fallback to human or canned responses

## Common failure
- letting the LLM answer without grounding
- no evaluation or monitoring strategy