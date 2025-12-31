from acm.core.agent_loop import AgentLoop
from acm.core.fake_llm import FakeLLMProvider



agent = AgentLoop(llm_provider=FakeLLMProvider())


print("---- RUN 1 ----")
r1 = agent.run("User reports login timeout error")
print(r1)

print("\n---- RUN 2 ----")
r2 = agent.run("Investigate the same login issue again")
print(r2)

print("\n---- RUN 3 ----")
r3 = agent.run("What do we know so far about the login issue?")
print(r3)

print("\nMEMORY COUNT:", len(agent.memories))

