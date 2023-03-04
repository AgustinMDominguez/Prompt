import openai

from src.models import ModelFinder
from src.ai.config import COMPLETION_DEFAULT_TEMPERATURE, COMPLETION_DEFAULT_MAX_TOKENS


def complete_prompt(
    input: str,
    temperature: float = COMPLETION_DEFAULT_TEMPERATURE,
    max_tokens: int = COMPLETION_DEFAULT_MAX_TOKENS,
    echo_prompt: bool = True
) -> str:
    response = openai.Completion.create(
        model=ModelFinder.get_strongest().as_str,
        prompt=input,
        temperature=temperature,
        max_tokens=max_tokens,
        echo=echo_prompt
    )
    print(f"Temperature: {temperature}\tmax_tokens: {max_tokens}")
    return response.choices[0].text
