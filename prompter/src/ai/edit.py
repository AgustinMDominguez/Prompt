import openai
from src.models import ModelFinder
from src.ai.config import EDIT_DEFAULT_TEMPERATURE


class EditPromptResult:
    def __init__(self, result: str, used_tokens: int) -> None:
        self.result = result
        self.used_tokens = used_tokens


def edit_prompt(
    source: str,
    instruction: str,
    temperature: float = EDIT_DEFAULT_TEMPERATURE
) -> EditPromptResult:
    if source is None or instruction is None:
        return EditPromptResult(None, 0)
    response = openai.Edit.create(
        model=ModelFinder.get_edit_model().as_str,
        input=source,
        instruction=instruction,
        temperature=temperature
    )
    result = EditPromptResult(
        result=response.choices[0].text,
        used_tokens=response.usage.total_tokens
    )
    return result
