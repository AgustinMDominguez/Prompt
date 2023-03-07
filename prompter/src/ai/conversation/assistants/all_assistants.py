from src.ai.conversation.assistants.assistant import Assistant
from src.ai.conversation.assistants.blake import Blake
from src.ai.conversation.assistants.grace import Grace


ALL_ASSISTANTS = [Blake, Grace]


def map_assistant(assistant_name):
    assistants: list[Assistant] = ALL_ASSISTANTS
    for assistant in assistants:
        if assistant_name == assistant._name:
            return assistant()
