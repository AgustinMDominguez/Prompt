from argparse import Namespace
from src.prompter.input import InputFetcher, PromptInput

class CommandLineInputFetcher(InputFetcher):
    def __init__(self, args: list = [], kwargs: dict = {}) -> None:
        self.args: list = args
        self.kwargs: dict = kwargs
        super().__init__()

    def extract_arguments(self, parse_result: Namespace) -> None:
        raise NotImplementedError(
            "Method extract_arguments of base class ArgumentExtractor Not Implemented"
        )

    def extract_default_input(self, parse_result: Namespace):
        if parse_result.prompt is not None:
            self.args.append(parse_result.prompt)
        else:
            if parse_result.input is not None:
                with open(parse_result.input, 'r') as f:
                    lines = f.readlines()
                    prompt = "\n".join(lines)
                    self.args.append(prompt)

    def get_input(self) -> PromptInput:
        return PromptInput(self.args, self.kwargs)
