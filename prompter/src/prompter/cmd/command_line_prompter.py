import argparse
from argparse import Namespace
from src.prompter.prompter import Prompter
from src.prompter.input import PromptInput, InputFetcher
from src.prompter.output import PromptOutput, OutputWriter
from src.prompter.prompt_executor import PromptExecutor
from src.prompter.parsers.echo_parser import EchoParser
from prompter.src.prompter.cmd.command_line_input_fetcher import CommandLineInputFetcher


class PromptArgs:
    def __init__(self, args: list = [], kwargs: dict = {}) -> None:
        self.args: list = args
        self.kwargs: dict = kwargs


class CommandLineOutputWriter(OutputWriter):

    def __init__(self) -> None:
        self.output_filename = None
        super().__init__()

    def write_output(self, output: PromptOutput):
        if output.result is not None:
            self._write(output.result)
        else:
            self._write("<|endoftext|>")
        if output.tokens_used is not None:
            self._write(f"Total tokens used: {output.tokens_used}")

    def _write(self, string: str):
        if self.output_filename is not None:
            with open(self.output_filename, 'w') as f:
                f.write(string + "\n")
        else:
            print(string)


class CommandLinePrompter(Prompter):
    def __init__(self) -> None:
        self.argument_parser = argparse.ArgumentParser()
        self.subparsers = self.argument_parser.add_subparsers()
        command_parsers = [
            EchoParser()
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
