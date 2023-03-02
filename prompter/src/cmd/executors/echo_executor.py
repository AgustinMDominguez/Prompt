from src.cmd.prompt_executor import PromptExecutor
from src.cmd.input import PromptInput
from src.cmd.output import PromptOutput
from src.ai.echo import echo

class EchoExecutor(PromptExecutor):
    def execute(self, input: PromptInput) -> PromptOutput:
        result = echo(*input.args)
        return PromptOutput(result=result, tokens_used=0)

