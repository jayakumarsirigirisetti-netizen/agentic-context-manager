from acm import Agent

agent = Agent(
    goal="Debug backend authentication issues",
    llm="fake"  # change to "openai" later
)

print(agent.run("User reports login timeout error"))
print(agent.run("Investigate the same issue again"))
print(agent.run("What do we know so far?"))

print("Memory count:", agent.memory_count())

