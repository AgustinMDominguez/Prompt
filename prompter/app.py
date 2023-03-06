import os
import openai
from src.prompter.cmd.command_line_prompter import CommandLinePrompter


openai.api_key = os.getenv("OPENAI_API_KEY")


def test():
    from src.ai.conversation.assistants import Blake
    assistant = Blake()
    # print(assistant.get_current_date())
    # print(assistant.get_system_message())
    from src.ai.conversation.chat_manager import ChatManager
    manager = ChatManager(assistant)
    manager.run()


def main():
    # prompter = CommandLinePrompter()
    # prompter.execute_prompt()
    test()


if __name__ == "__main__":
    main()
