import openai

from src.models import ModelFinder
from src.ai.config import CHAT_DEFAULT_TEMPERATURE
from src.ai.conversation.message import (
    ChatHistory,
    ChatMessage
)


def iterate_chat(history: ChatHistory, temperature=CHAT_DEFAULT_TEMPERATURE) -> ChatMessage:
    messages = [msg.to_dict() for msg in history.messages]
    response = openai.ChatCompletion.create(
        model=ModelFinder.get_chat_model().as_str,
        messages=messages,
        temperature=temperature
    )
    message = response.choices[0].message
    return ChatMessage(message.role, message.content)
