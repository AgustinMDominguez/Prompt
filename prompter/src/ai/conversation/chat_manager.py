from src.ai.conversation.assistants import Assistant
from src.ai.conversation.message import ChatHistory, UserMessage, SystemMessage
from src.ai.conversation.chat import iterate_chat
from src.ai.config import CHAT_DEFAULT_TEMPERATURE


class ChatManager:
    def __init__(
        self, assistant: Assistant,
        temperature: float = CHAT_DEFAULT_TEMPERATURE
    ) -> None:
        self.token_used = 0
        self.close_message = "close"
        self.temperature = temperature
        self.assistant = assistant
        init_msg = SystemMessage(self.assistant.get_system_message())
        self.history = ChatHistory([init_msg])

    def run(self):
        first_message = SystemMessage("Start with your name and ask what can you help with")
        self.history.messages.append(first_message)
        self.fetch_response()
        self.print_last_message()
        while True:
            user_message = UserMessage(input("\t -> "))
            if user_message.content.lower().strip() == self.close_message:
                break
            self.history.messages.append(user_message)
            self.fetch_response()
            self.print_last_message()
        print("Chat finished")

    def print_last_message(self):
        print(f"[{self.assistant.name}] :: {self.history.messages[-1].content}")

    def fetch_response(self):
        response = iterate_chat(self.history, self.temperature)
        self.history.messages.append(response)

    def get_total_use(self) -> int:
        return self.token_used
