from src.ai.conversation.assistants.assistant import Assistant


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
