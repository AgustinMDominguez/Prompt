import openai

from src.models import ModelFinder
from src.ai.config import COMPLETION_DEFAULT_TEMPERATURE, COMPLETION_DEFAULT_MAX_TOKENS


class CompletePromptResult:
    def __init__(self, result: str, used_tokens: int) -> None:
        self.result = result
        self.used_tokens = used_tokens

    def __str__(self) -> str:
        return f"OsResponse(result={self.result}, tokens_used:{self.used_tokens})"


def complete_prompt(
    input: str,
    temperature: float = COMPLETION_DEFAULT_TEMPERATURE,
    max_tokens: int = COMPLETION_DEFAULT_MAX_TOKENS,
    echo_prompt: bool = True
) -> CompletePromptResult:
    response = openai.Completion.create(
        model=ModelFinder.get_strongest().as_str,
        prompt=input,
        temperature=temperature,
        max_tokens=max_tokens,
        echo=echo_prompt
    )
    result = CompletePromptResult(
        result=response.choices[0].text,
        used_tokens=response.usage.total_tokens
    )
    return result
