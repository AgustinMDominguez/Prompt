import openai

from src.models import ModelFinder

from src.ai.config import CODE_DEFAULT_MAX_TOKENS, CODE_DEFAULT_TEMPERATURE


class CodePromptResult:
    def __init__(self, result: str, used_tokens: int) -> None:
        self.result = result
        self.used_tokens = used_tokens


def code_prompt(
    input: str,
    temperature: float = CODE_DEFAULT_TEMPERATURE,
    max_tokens: int = CODE_DEFAULT_MAX_TOKENS,
    echo_prompt: bool = True
) -> CodePromptResult:
    response = openai.Completion.create(
        model=ModelFinder.get_best_for_code().as_str,
        prompt=input,
        temperature=temperature,
        max_tokens=max_tokens,
        echo=echo_prompt
    )
    result = CodePromptResult(
        result=response.choices[0].text,
        used_tokens=response.usage.total_tokens
    )
    return result
