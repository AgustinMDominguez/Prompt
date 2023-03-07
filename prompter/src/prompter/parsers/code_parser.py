from argparse import ArgumentParser, Namespace

from src.prompter.parsers.command_parser import CommandParser
from src.prompter.executors.code_executor import CodeExecutor
from src.prompter.cmd.command_line_input_fetcher import CommandLineInputFetcher
from src.prompter.cmd.command_line_help import (
    CODE_COMMAND_HELP,
    TEMPERATURE_FLAG_HELP,
    MAX_TOKENS_FLAG_HELP
)


class CodeParser(CommandParser):

    def __init__(self) -> None:
        super().__init__("code")

    def add_command_subparser(self, subparsers):
        code_parser: ArgumentParser = subparsers.add_parser(
            self.command_name,
            help=CODE_COMMAND_HELP
        )
        self.add_default_input_argument(code_parser)
        self.add_default_output_argument(code_parser)
        code_parser.add_argument("prompt", nargs='?')
        code_parser.add_argument("--temperature", "-t", type=float, help=TEMPERATURE_FLAG_HELP)
        code_parser.add_argument("--maxtokens", "-k", type=int, help=MAX_TOKENS_FLAG_HELP)
        code_parser.set_defaults(
            executor=CodeExecutor(),
            input_fetcher=CodeInputFetcher()
        )


class CodeInputFetcher(CommandLineInputFetcher):
    def extract_arguments(self, parse_result: Namespace) -> None:
        self.extract_default_input(parse_result)
        if parse_result.temperature is not None:
            self.kwargs["temperature"] = parse_result.temperature
        if parse_result.maxtokens:
            self.kwargs["max_tokens"] = parse_result.maxtokens
