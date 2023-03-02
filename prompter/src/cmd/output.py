
class PromptOutput:
    def __init__(self, result: str = "", tokens_used: int = None) -> None:
        self.result = result
        self.tokens_used = tokens_used


class OutputWriter:
    def write_output(self, output: PromptOutput):
        raise NotImplementedError(
            "write_output of base class OutputWriter not implemented"
        )
