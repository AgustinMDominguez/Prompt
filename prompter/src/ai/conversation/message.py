
class ChatMessage:
    def __init__(self, role: str, content: str) -> None:
        self.role = role
        self.content = content

    def to_dict(self) -> dict:
        return {"role": self.role, "content": self.content}


class UserMessage(ChatMessage):
    _role = "user"
    def __init__(self, content: str) -> None:
        super().__init__(self._role, content)


class SystemMessage(ChatMessage):
    _role = "system"
    def __init__(self, content: str) -> None:
        super().__init__(self._role, content)


class AssistantMessage(ChatMessage):
    _role = "assistant"
    def __init__(self, content: str) -> None:
        super().__init__(self._role, content)


class ChatHistory:
    def __init__(self, messages: list[ChatMessage]) -> None:
        self.messages = messages
