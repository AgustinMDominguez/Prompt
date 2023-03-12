import subprocess

from src.ai.config import OS_DEFAULT_TEMPERATURE
from src.ai.conversation.chat import iterate_chat
from src.ai.completion import complete_prompt
from src.ai.conversation.message import (
    ChatHistory,
    SystemMessage,
    UserMessage
)


DEBUG = False


class OsResponse():
    def __init__(self, result: str, tokens_used: int = 0) -> None:
        self.result = result
        self.used_tokens = tokens_used

    def __str__(self) -> str:
        return f"OsResponse(result={self.result}, tokens_used:{self.used_tokens})"


class OsInterpreter:
    LANGUAGES = {
        "bash": "bash",
        "PowerShell": "bash",
        "python": "python"
    }

    def __init__(self, prompt, temperature: float = OS_DEFAULT_TEMPERATURE) -> None:
        self.temperature = temperature
        self.prompt = prompt
        self.total_tokens = 0
        self.chosen_language: str = None

    def execute_prompt(self) -> OsResponse:
        self.select_language()
        self.debug(f"Os chose {self.chosen_language} as scripting language")
        script = self.get_script()
        self.debug(f"script: '{script}'")
        execution = self.execute_script(script)
        self.debug(f"execution: {execution}")
        result = self.get_response(execution, script)
        return OsResponse(result=result, tokens_used=self.total_tokens)

    def select_language(self):
        response = complete_prompt(
            self.get_language_prompt(self.prompt),
            temperature=0.1,
            echo_prompt=False
        )
        self.add_tokens(response.used_tokens)
        self.chosen_language = self.LANGUAGES[response.result.strip().lower()]

    def get_script(self) -> str:
        response = complete_prompt(
            self.get_scripting_prompt(self.prompt, self.chosen_language),
            temperature=self.temperature,
            echo_prompt=False
        )
        self.add_tokens(response.used_tokens)
        return response.result.strip()

    def execute_script(self, script) -> str:
        executors = {
            self.LANGUAGES["bash"]: self.execute_shell_script,
            self.LANGUAGES["python"]: self.execute_python_script,
        }
        executor = executors[self.chosen_language]
        return executor(script).strip()

    def execute_python_script(self, script) -> str:
        "TODO! PYTHON RESULT"

    def execute_shell_script(self, command) -> str:
        result = subprocess.run(command, stdout=subprocess.PIPE, shell=True)
        return result.stdout.decode('utf-8')

    def get_response(self, execution_result, script) -> str:
        messages = [
            SystemMessage("You are a helpful assistant. Answer only what you are asked and use the system response"),
            UserMessage(self.prompt),
            SystemMessage(f"Running {script} returns: {execution_result}")
        ]
        history = ChatHistory(messages)
        assistant_response = iterate_chat(history, temperature=self.temperature)
        return assistant_response.content

    def add_tokens(self, amount_tokens):
        self.total_tokens += amount_tokens

    def debug(self, msg):
        if DEBUG:
            print(msg)

    def get_scripting_prompt(self, question: str, language: str):
        prompts = {
            self.LANGUAGES["bash"]: f'Write a Bash command to answer the question "{question}".',
            self.LANGUAGES["python"]: f'Write a Python script to answer the question "{question}".'
        }
        return prompts[language]

    @staticmethod
    def get_language_prompt(question: str):
        sentences = [
            f'What would be the best scripting language to answer the question "{question}".'
            f'Write just the language name'
        ]
        return " ".join(sentences)

    @staticmethod
    def get_final_result(question: str, script_output: str):
        sentences = [
            f'System response:\n"{script_output}"\nUser Question:',
            f'\n"{question}".\n Assistant answer:'
        ]
        return " ".join(sentences)
