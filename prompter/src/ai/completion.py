import openai

from modules.models import ModelFinder
from modules.CommandParser import CommandParser


def get_command_parser() -> CommandParser:
    completion_command_parser = CommandParser("ask")
    completion_command_parser.executor = complete_prompt
    return completion_command_parser


def complete_prompt(input: str) -> str:
    response = openai.Completion.create(
        model=ModelFinder.get_strongest().as_str,
        prompt=input,
        temperature=0.2,
        max_tokens=200,
        echo=True
    )
    print(f"Token used in total: {response.usage.total_tokens}")
    return response.choices[0].text
