from acm.core.agent_loop import AgentLoop
from acm.core.fake_llm import FakeLLMProvider
from acm.core.llm_provider import OpenAIProvider


class Agent:
    """
    Public SDK Agent.
    Clean interface over the internal agent loop.
    """

    def __init__(
        self,
        goal: str,
        llm: str = "fake",
    ):
        """
        goal: High-level agent goal (used for context priming)
        llm: "fake" (default) or "openai"
        """

        self.goal = goal

        if llm == "openai":
            self.loop = AgentLoop(llm_provider=OpenAIProvider())
        else:
            self.loop = AgentLoop(llm_provider=FakeLLMProvider())

        # Store the goal as initial memory
        self.loop.store_response(
            task="Agent goal initialization",
            response=f"Agent goal: {goal}"
        )

    def run(self, task: str) -> str:
        """
        Run the agent on a task.
        """
        return self.loop.run(task)

    def memory_count(self) -> int:
        """
        For debugging / inspection.
        """
        return len(self.loop.memories)

