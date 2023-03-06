from argparse import ArgumentParser, Namespace

from src.prompter.parsers.command_parser import CommandParser
from src.prompter.executors.ask_executor import AskExecutor
from src.prompter.cmd.command_line_input_fetcher import CommandLineInputFetcher
from src.prompter.cmd.command_line_help import (
    TEMPERATURE_FLAG_HELP,
    MAX_TOKENS_FLAG_HELP,
    ASK_COMMAND_HELP
)


class AskParser(CommandParser):

    def __init__(self) -> None:
        super().__init__("ask")

    def add_command_subparser(self, subparsers):
        ask_parser: ArgumentParser = subparsers.add_parser(self.command_name, help=ASK_COMMAND_HELP)
        self.add_default_input_argument(ask_parser)
        self.add_default_output_argument(ask_parser)
        ask_parser.add_argument("prompt", nargs='?', default=None)
        ask_parser.add_argument("--temp", "-t", type=float, help=TEMPERATURE_FLAG_HELP)
        ask_parser.add_argument("--maxtokens", "-k", type=int, help=MAX_TOKENS_FLAG_HELP)
        ask_parser.set_defaults(
            executor=AskExecutor(),
            input_fetcher=AskInputFetcher()
        )


class AskInputFetcher(CommandLineInputFetcher):
    def extract_arguments(self, parse_result: Namespace) -> None:
        self.extract_default_input(parse_result)
        if parse_result.temp is not None:
            self.kwargs["temperature"] = parse_result.temp
        if parse_result.maxtokens:
            self.kwargs["max_tokens"] = parse_result.maxtokens
