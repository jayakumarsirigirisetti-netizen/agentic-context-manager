class FakeLLMProvider:
    def __init__(self):
        self.turn = 0

    def complete(self, prompt: str) -> str:
        self.turn += 1

        if self.turn == 1:
            return "Login timeout may be caused by backend latency or auth service downtime. Check logs."
        elif self.turn == 2:
            return "Previously we suspected backend latency. Investigate auth service logs and database timeouts."
        else:
            return "So far, we observed login timeout errors likely related to backend latency and auth service issues."

