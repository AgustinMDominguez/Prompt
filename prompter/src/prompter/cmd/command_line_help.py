
ECHO_COMMAND_HELP = """test command that just repeats the input prompt.
 'ai echo -h' for more details"""
ASK_COMMAND_HELP = """basic commands for the strongest model for prompt completion.
Can do questions and natural language commands. 'ai ask -h' for more details"""
EDIT_COMMAND_HELP = "TODO!! EDIT_COMMAND_HELP"
CODE_COMMAND_HELP = """performs completion commands like 'ask' but tuned
specifically for code completion. ai code -h' for more details"""
CHAT_COMMAND_HELP = """starts a chat with one of the available assistants that
 will try to help the user. ai chat -h' for more details"""
OS_COMMAND_HELP = """Runs a background ai generated script to perform a simple ask.
 ai chat -h' for more details"""

# Flags

TEMPERATURE_FLAG_HELP = """temperature affects the randomness of the output.
A lower temperature will result in more predictable output,
while a higher temperature will result in more random output"""

MAX_TOKENS_FLAG_HELP = """limits the amount of tokens that are used in the request.
Tokens are pieces of words.
1 token ~= 4 chars in English | 1 token ~= 3/4 words | 100 tokens ~= 75 words"""

DEFAULT_INPUT_ARGUMENT_HELP = "file path from where the input should be read"
DEFAULT_OUTPUT_ARGUMENT_HELP = "file path from where the result will be written"

INSTRUCTION_FLAG_HELP = "instruction to what will be done to the source text"
SOURCE_ARGUMENT_HELP = "the text that will be edited. It can be replaced with the -i flag"

ASSISTANT_ARGUMENT_HELP = """
 Blake: General assistant with the most knowledge.
 Grace: More concise assistant that doesn't know code or other languages."""
