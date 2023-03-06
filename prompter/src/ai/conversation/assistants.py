from datetime import datetime
from src.ai.conversation.message import SystemMessage


class Assistant:

    def __init__(self) -> None:
        self.name = "Assistant"
        self.system_message_parts = ["You are an assistant."]

    def get_system_message(self) -> SystemMessage:
        return ". ".join(self.system_message_parts)

    def get_current_date(self) -> str:
        now = datetime.now()
        return now.strftime("%A %d. %B %Y") + f" at around {now.hour} hs"


class Blake(Assistant):
    def __init__(self) -> None:
        self.name = "Blake"
        personality_traits = [
            f"You are {self.name},"
            "a very hepful, calm, and curious assistant made by Agustin.",
            "You are nonpartisan, genderless, and very knowledgeable on most topics.",
            "You can speak spanish",
        ]
        chat_context = [
            f"Today is {self.get_current_date()}"
        ]
        instructions = [
            "Answer as truthfully as you can,",
            """say "I don't know" when you are not sure"""
        ]
        personality = " ".join(personality_traits)
        context = " ".join(chat_context)
        instructions = " ".join(instructions)
        self.system_message_parts = [personality, context, instructions]
