
class CommandParser:
    def __init__(self, command_name) -> None:
        self.command_name = command_name
        self.executor = None
