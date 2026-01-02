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
Results so far
--------------

In our own agent runs:

- Naive agent tokens per run: **30,670**
- ACM agent tokens per run: **3,191**
- Net reduction: **~89%** tokens

Even on a modest production load, this translates to:

- 10K runs/month → ~275M tokens saved
- At $3 per million tokens → **$800+/month** saved for a single workflow

(These are early internal numbers; we are actively validating with external teams.)


## The Solution

Agentic Context Manager introduces a dedicated **context layer** that:

- Stores long-term memory in vector space (FAISS)
- Retrieves only relevant context per step
- Keeps prompts minimal and focused
- Decouples memory from the LLM call
- Makes agent cost scale sub-linearly with time

This is infrastructure, not a wrapper.

---
Who is ACM for?
---------------

ACM is built for teams running **long‑lived or multi‑step agents** in production, for example:

- Support / success copilots running 50–500 conversations per day
- Workflow / ops agents executing 10–50 steps per ticket
- Research / analysis agents that read large corpora over many turns

If you are spending **$1K+/month on LLM APIs** and see context windows or cost exploding as agents scale, ACM is designed for you.

Architecture (high level)
-------------------------

ACM sits **between your agent loop and the LLM**:

User → Orchestrator / Agent Framework → **ACM (store/retrieve)** → LLM API

Core components:

- `MemoryStore`: FAISS‑backed vector store for long‑term memory
- `DecayEngine`: configurable decay of stale or low‑value memory
- `Summarizer`: periodic summarization to keep memory bounded
- `HealthCheck`: lightweight service to inspect memory size and status

Roadmap
-------

Short-term:

- LangChain / CrewAI / Autogen integration examples
- Simple dashboard to visualize memory size and token savings
- More benchmark scenarios (tools-heavy agents, RAG + agents, etc.)

Medium-term:

- Multi-tenant memory server
- Hosted ACM with metrics, alerts, and per-team cost dashboards

Why now?
--------

- Agent frameworks (LangChain, CrewAI, Autogen, etc.) are moving from demos to production.
- LLM prices are dropping per token, but **total spend is exploding** as agents get more complex and run longer.
- Most teams are still hacking memory inside prompts; very few have dedicated context infra.

ACM exists because **agents are scaling faster than their memory architecture**. We want to be the default memory layer for AI-native products.

Quickstart
----------

1. Install

```bash
pip install agentic-context-manager   # if you publish to PyPI
# or
git clone https://github.com/jayakumarsirigirisetti-netizen/agentic-context-manager.git
cd agentic-context-manager
pip install -r requirements.txt


2.Run health check
python health_check.py
# ✅ prints current memory size and confirms FAISS index is reachable
from acm import AgenticContextManager

3.Use in your agent loop 
acm = AgenticContextManager(memory_dir="acm_memory")

# 1. After each step, store what's important
acm.store(step_id="step_1", text=agent_response)

# 2. Before each new LLM call, fetch only relevant context
relevant_context = acm.retrieve(query=user_query, top_k=5)

llm_input = f"{relevant_context}\n\nUser: {user_query}\nAssistant:"

4.Persist and restore between runs
acm.save()     # persist vector store to disk
acm.load()     # restore on reboot

