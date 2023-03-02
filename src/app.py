# library imports
import os
import openai

# local imports
from modules.completion import complete_prompt


openai.api_key = os.getenv("OPENAI_API_KEY")

def get_prompt() -> str:
    with open("input.txt", "r") as f:
        lines = f.readlines()
        return "\n".join(lines)


def write_output(output: str):
    with open("output.txt", 'w') as f:
        f.write(output)


def main():
    input = get_prompt()
    write_output(complete_prompt(input))


if __name__ == "__main__":
    main()
