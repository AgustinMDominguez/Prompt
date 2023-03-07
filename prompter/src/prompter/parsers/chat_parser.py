from argparse import ArgumentParser, Namespace

from src.prompter.parsers.command_parser import CommandParser
from src.prompter.executors.chat_executor import ChatExecutor
from src.prompter.cmd.command_line_input_fetcher import CommandLineInputFetcher
from src.ai.conversation.assistants import all_assistants, Assistant
from src.prompter.cmd.command_line_help import (
    TEMPERATURE_FLAG_HELP,
    ASSISTANT_ARGUMENT_HELP,
    CHAT_COMMAND_HELP
)


class ChatParser(CommandParser):

    def __init__(self) -> None:
        super().__init__("chat")

    def add_command_subparser(self, subparsers):
        chat_parser: ArgumentParser = subparsers.add_parser(
            self.command_name,
            help=CHAT_COMMAND_HELP
        )
        self.add_default_output_argument(chat_parser)
        assistants = [assistant._name for assistant in all_assistants]
        chat_parser.add_argument("assistant", choices=assistants, help=ASSISTANT_ARGUMENT_HELP)
        chat_parser.add_argument("--temperature", "-t", type=float, help=TEMPERATURE_FLAG_HELP)
        chat_parser.set_defaults(
            executor=ChatExecutor(),
            input_fetcher=ChatInputFetcher()
        )


class ChatInputFetcher(CommandLineInputFetcher):
    def extract_arguments(self, parse_result: Namespace) -> None:
        self.args.append(Assistant.map_assistant(parse_result.assistant))
        if parse_result.temperature is not None:
            self.kwargs["temperature"] = parse_result.temperature
