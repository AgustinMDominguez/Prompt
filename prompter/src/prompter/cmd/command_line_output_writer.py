from src.prompter.output import OutputWriter, PromptOutput


class CommandLineOutputWriter(OutputWriter):

    def __init__(self) -> None:
        self.output_filename = None
        super().__init__()

    def write_output(self, output: PromptOutput):
        if self.output_filename is not None:
            self._clean_output_file()
        if output.result is not None:
            self._write(output.result)
        else:
            self._write("<|endoftext|>")
        if output.tokens_used is not None:
            self._write(f"\n[Total tokens used: {output.tokens_used}]")

    def _write(self, string: str):
        if self.output_filename is not None:
            with open(self.output_filename, 'a') as f:
                f.write(string)
        else:
            print(string)

    def _clean_output_file(self):
        with open(self.output_filename, 'w') as f:
            f.write("")
