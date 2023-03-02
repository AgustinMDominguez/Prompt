from argparse import ArgumentParser, Namespace

from src.cmd.parsers.command_parser import CommandParser
from src.cmd.executors.echo_executor import EchoExecutor
from src.cmd.command_line_input_fetcher import CommandLineInputFetcher


class EchoParser(CommandParser):

    def __init__(self) -> None:
        super().__init__("echo")

    def add_command_subparser(self, subparsers):
        echo_parser = subparsers.add_parser(self.command_name)
        self.add_default_input_argument(echo_parser)
        self.add_default_output_argument(echo_parser)
        echo_parser.add_argument("prompt", nargs='?', default=None)
        echo_parser.set_defaults(
            executor = EchoExecutor(),
            input_fetcher = EchoInputFetcher()
        )


class EchoInputFetcher(CommandLineInputFetcher):
    def extract_arguments(self, parse_result: Namespace) -> None:
        if parse_result.prompt is not None:
            self.args.append(parse_result.prompt)
        else:
            if parse_result.input is not None:
                with open(parse_result.input, 'r') as f:
                    lines = f.readlines()
                    prompt = "\n".join(lines)
                    self.args.append(prompt)
