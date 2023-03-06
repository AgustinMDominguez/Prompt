from src.prompter.input import InputFetcher
from src.prompter.output import OutputWriter
from src.prompter.prompt_executor import PromptExecutor


class Prompter:
    def __init__(
        self,
        input_fetcher: InputFetcher,
        output_writer: OutputWriter,
        prompt_executor: PromptExecutor
    ) -> None:
        self.input_fetcher: InputFetcher = input_fetcher
        self.output_writer: OutputWriter = output_writer
        self.prompt_executor: PromptExecutor = prompt_executor

    def execute_prompt(self):
        input = self.input_fetcher.get_input()
        output = self.prompt_executor.execute(input)
        self.output_writer.write_output(output)
