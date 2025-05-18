class DeterministicAgent:
    """A simple deterministic agent with fixed responses."""

    def respond(self, user_input: str) -> str:
        text = user_input.strip().lower()
        if text == "hello":
            return "Ciao! Come posso aiutarti?"
        if text == "bye" or text == "goodbye":
            return "Arrivederci!"
        return "Sono un agente deterministico."
