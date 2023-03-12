from src.prompter.input import PromptInput
from src.prompter.output import PromptOutput
from src.ai.os import OsInterpreter
from src.prompter.prompt_executor import PromptExecutor


class OsExecutor(PromptExecutor):
    def execute(self, input: PromptInput) -> PromptOutput:
        interpreter = OsInterpreter(*input.args, **input.kwargs)
        result = interpreter.execute_prompt()
        return PromptOutput(result=result.result, tokens_used=result.used_tokens)
