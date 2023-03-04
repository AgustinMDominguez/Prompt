from argparse import ArgumentParser, Namespace

from src.prompter.parsers.command_parser import CommandParser
from src.prompter.executors.echo_executor import EchoExecutor
from src.prompter.cmd.command_line_input_fetcher import CommandLineInputFetcher


class EchoParser(CommandParser):

    def __init__(self) -> None:
        super().__init__("echo")

    def add_command_subparser(self, subparsers):
        echo_parser: ArgumentParser = subparsers.add_parser(self.command_name)
        self.add_default_input_argument(echo_parser)
        self.add_default_output_argument(echo_parser)
        echo_parser.add_argument("prompt", nargs='?')
        echo_parser.set_defaults(
            executor = EchoExecutor(),
            input_fetcher = EchoInputFetcher()
        )


class EchoInputFetcher(CommandLineInputFetcher):
    def extract_arguments(self, parse_result: Namespace) -> None:
        self.extract_default_input(parse_result)