from src.prompter.input import PromptInput
from src.prompter.output import PromptOutput
from src.ai.completion import complete_prompt
from src.prompter.prompt_executor import PromptExecutor


class AskExecutor(PromptExecutor):
    def execute(self, input: PromptInput) -> PromptOutput:
        result = complete_prompt(*input.args, **input.kwargs)
        return PromptOutput(result=result.result, tokens_used=result.used_tokens)
