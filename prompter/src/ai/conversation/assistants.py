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

    @classmethod
    def map_assistant(cls, assistant_name):
        assistants: list[Assistant] = [Blake, Stace]
        for assistant in assistants:
            if assistant_name == assistant._name:
                return assistant()


class Blake(Assistant):
    _name = "Blake"

    def __init__(self) -> None:
        self.name = self._name
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


class Stace(Assistant):
    _name = "Stace"

    def __init__(self) -> None:
        self.name = self._name
        personality_traits = [
            f"You are {self.name},"
            "a tired middle age female secretary.",
            "Pretend you are human. You are not very knowlegable and not that polite,",
            "but you try to help. You only speak English",
        ]
        chat_context = [
            f"Today is {self.get_current_date()}"
        ]
        instructions = [
            "Make your answers brief."
        ]
        personality = " ".join(personality_traits)
        context = " ".join(chat_context)
        instructions = " ".join(instructions)
        self.system_message_parts = [personality, context, instructions]


all_assistants = [Blake, Stace]
