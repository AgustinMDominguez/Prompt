from argparse import ArgumentParser, Namespace

from src.prompter.parsers.command_parser import CommandParser
from src.prompter.executors.os_executor import OsExecutor
from src.prompter.cmd.command_line_input_fetcher import CommandLineInputFetcher
from src.prompter.cmd.command_line_help import (
    TEMPERATURE_FLAG_HELP,
    OS_COMMAND_HELP
)


class OsParser(CommandParser):

    def __init__(self) -> None:
        super().__init__("os")

    def add_command_subparser(self, subparsers):
        ask_parser: ArgumentParser = subparsers.add_parser(self.command_name, help=OS_COMMAND_HELP)
        self.add_default_input_argument(ask_parser)
        self.add_default_output_argument(ask_parser)
        ask_parser.add_argument("prompt", nargs='?')
        ask_parser.add_argument("--temperature", "-t", type=float, help=TEMPERATURE_FLAG_HELP)
        ask_parser.set_defaults(
            executor=OsExecutor(),
            input_fetcher=OsInputFetcher()
        )


class OsInputFetcher(CommandLineInputFetcher):
    def extract_arguments(self, parse_result: Namespace) -> None:
        self.extract_default_input(parse_result)
        if parse_result.temperature is not None:
            self.kwargs["temperature"] = parse_result.temperature
