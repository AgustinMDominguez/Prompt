from src.ai.code import code_prompt
from src.prompter.input import PromptInput
from src.prompter.output import PromptOutput
from src.prompter.prompt_executor import PromptExecutor


class CodeExecutor(PromptExecutor):
    def execute(self, input: PromptInput) -> PromptOutput:
        result = code_prompt(*input.args, **input.kwargs)
        return PromptOutput(result=result.result, tokens_used=result.used_tokens)
