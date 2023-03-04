from argparse import ArgumentParser, Namespace

class CommandParser:

    def __init__(self, command_name: str) -> None:
        self.command_name = command_name

    def add_command_subparser(self, subparsers):
        raise NotImplementedError(
            "add_command_subparser for base class CommandParser Not Implemented"
        )

    def add_default_input_argument(self, parser: ArgumentParser):
        parser.add_argument("--output", "-o", default=None)

    def add_default_output_argument(self, parser: ArgumentParser):
        parser.add_argument("--input", "-i", default=None)
