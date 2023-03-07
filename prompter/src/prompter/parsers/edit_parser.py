from argparse import ArgumentParser, Namespace

from src.prompter.parsers.command_parser import CommandParser
from src.prompter.executors.edit_executor import EditExecutor
from src.prompter.cmd.command_line_input_fetcher import CommandLineInputFetcher
from src.prompter.cmd.command_line_help import (
    EDIT_COMMAND_HELP,
    TEMPERATURE_FLAG_HELP,
    INSTRUCTION_FLAG_HELP
)


class EditParser(CommandParser):

    def __init__(self) -> None:
        super().__init__("edit")

    def add_command_subparser(self, subparsers):
        edit_parser: ArgumentParser = subparsers.add_parser(
            self.command_name,
            help=EDIT_COMMAND_HELP
        )
        self.add_default_input_argument(edit_parser)
        self.add_default_output_argument(edit_parser)
        edit_parser.add_argument("source", nargs='?')
        edit_parser.add_argument("instruction", help=INSTRUCTION_FLAG_HELP)
        edit_parser.add_argument("--temperature", "-t", type=float, help=TEMPERATURE_FLAG_HELP)
        edit_parser.set_defaults(
            executor=EditExecutor(),
            input_fetcher=EditInputFetcher()
        )


class EditInputFetcher(CommandLineInputFetcher):
    def extract_arguments(self, parse_result: Namespace) -> None:
        self.extract_source(parse_result)
        self.args.append(parse_result.instruction)
        if parse_result.temperature is not None:
            self.kwargs["temperature"] = parse_result.temperature

    def extract_source(self, parse_result):
        if parse_result.source is not None:
            self.args.append(parse_result.source)
        else:
            if parse_result.input is not None:
                with open(parse_result.input, 'r') as f:
                    lines = f.readlines()
                    prompt = "".join(lines)
                    self.args.append(prompt)
            else:
                self.args.append(None)
