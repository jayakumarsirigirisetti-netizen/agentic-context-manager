# Agentic Context Manager (ACM)

Agentic Context Manager (ACM) is an AI infrastructure library that reduces token usage for agentic systems by managing long-term context using vector memory instead of prompt stuffing.

As AI agents run longer and become multi-step, context becomes the real bottleneck — not models.

---

## The Problem

Most agentic systems fail to scale because:

- Context grows linearly with time
- Token costs explode
- Latency increases
- Context windows overflow
- Reasoning quality degrades with noisy prompts

Most teams try to solve this inside prompts.  
That approach does not scale.

---

## The Solution

Agentic Context Manager introduces a dedicated **context layer** that:

- Stores long-term memory in vector space (FAISS)
- Retrieves only relevant context per step
- Keeps prompts minimal and focused
- Decouples memory from the LLM call
- Makes agent cost scale sub-linearly with time

This is infrastructure, not a wrapper.

---

## Quickstart

```bash
git clone https://github.com/jayakumarsirigirisetti-netizen/agentic-context-manager.git
cd agentic-context-manager
python -m venv acm-env
source acm-env/bin/activate
pip install -r requirements.txt
python health_check.py
