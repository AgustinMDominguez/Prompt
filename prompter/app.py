# library imports
import os
import openai

# local imports
from src.prompter.cmd.command_line_prompter import CommandLinePrompter


openai.api_key = os.getenv("OPENAI_API_KEY")


def main():
    prompter = CommandLinePrompter()
    prompter.execute_prompt()


if __name__ == "__main__":
    main()
