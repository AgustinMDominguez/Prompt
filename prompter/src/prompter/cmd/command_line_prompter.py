import argparse
from src.prompter.prompter import Prompter
from src.prompter.input import InputFetcher
from src.prompter.output import OutputWriter
from src.prompter.prompt_executor import PromptExecutor
from src.prompter.cmd.command_line_input_fetcher import CommandLineInputFetcher
from src.prompter.cmd.command_line_output_writer import CommandLineOutputWriter

from src.prompter.parsers.echo_parser import EchoParser
from src.prompter.parsers.ask_parser import AskParser


class CommandLinePrompter(Prompter):
    def __init__(self) -> None:
        self.argument_parser = argparse.ArgumentParser()
        self.subparsers = self.argument_parser.add_subparsers()
        command_parsers = [
            EchoParser(),
            AskParser()
        ]

        for parser in command_parsers:
            parser.add_command_subparser(self.subparsers)

        super().__init__(
            input_fetcher = InputFetcher(),
            output_writer= OutputWriter(),
            prompt_executor= PromptExecutor()
        )

    def execute_prompt(self):
        parse_result = self.argument_parser.parse_args()
        self.prompt_executor: PromptExecutor = parse_result.executor
        self.output_writer: CommandLineOutputWriter = CommandLineOutputWriter()
        self.output_writer.output_filename = parse_result.output
        self.input_fetcher: CommandLineInputFetcher = parse_result.input_fetcher
        self.input_fetcher.extract_arguments(parse_result)
        return super().execute_prompt()
