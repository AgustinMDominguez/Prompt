from datetime import datetime
from src.ai.conversation.message import SystemMessage


class Assistant:
    _name = "Assistant"

    def __init__(self) -> None:
        self.name = self._name
        self.system_message_parts = ["You are an assistant."]

    def get_system_message(self) -> SystemMessage:
        return ". ".join(self.system_message_parts)

    def get_current_date(self) -> str:
        now = datetime.now()
        return now.strftime("%A %d. %B %Y") + f" at around {now.hour} hs"
