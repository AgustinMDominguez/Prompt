from src.prompter.input import PromptInput
from src.prompter.output import PromptOutput
from src.ai.edit import edit_prompt
from src.prompter.prompt_executor import PromptExecutor

class EditExecutor(PromptExecutor):
    def execute(self, input: PromptInput) -> PromptOutput:
        result = edit_prompt(*input.args, **input.kwargs)
        return PromptOutput(result=result.result, tokens_used=result.used_tokens)
