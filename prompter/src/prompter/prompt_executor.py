from src.prompter.input import PromptInput
from src.prompter.output import PromptOutput

class PromptExecutor:
    def execute(input: PromptInput) -> PromptOutput:
        raise NotImplementedError(
            "Method execute of base class PromptExecutor Not Implemented"
        )

