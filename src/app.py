# library imports
import os
import openai

# local imports
from modules.completion import some


openai.api_key = os.getenv("OPENAI_API_KEY")


def main():
    some()

if __name__ == "__main__":
    main()
