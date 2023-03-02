
class PromptInput:
    def __init__(self, args: list = [], kwargs: dict = {}):
        self.args = args
        self.kwargs = kwargs


class InputFetcher:
    def get_input(self) -> PromptInput:
        raise NotImplementedError(
            "get_input of base class InputFetcher not implemented"
        )
