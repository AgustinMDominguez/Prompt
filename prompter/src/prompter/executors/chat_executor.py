from src.prompter.input import PromptInput
from src.prompter.output import PromptOutput
from src.ai.conversation.chat_manager import ChatManager
from src.prompter.prompt_executor import PromptExecutor


class ChatExecutor(PromptExecutor):
    def execute(self, input: PromptInput) -> PromptOutput:
        manager = ChatManager(*input.args, **input.kwargs)
        manager.run()
        return PromptOutput()
