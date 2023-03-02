from argparse import Namespace
from src.cmd.input import InputFetcher, PromptInput

class CommandLineInputFetcher(InputFetcher):
    def __init__(self, args: list = [], kwargs: dict = {}) -> None:
        self.args: list = args
        self.kwargs: dict = kwargs
        super().__init__()

    def extract_arguments(self, parse_result: Namespace) -> None:
        raise NotImplementedError(
            "Method extract_arguments of base class ArgumentExtractor Not Implemented"
        )

    def get_input(self) -> PromptInput:
        return PromptInput(self.args, self.kwargs)
