This is a personal space for testing and developing Proofs of Concept for Application of the Open AI API.

# Links

* Installation & Setup: [(Español)](Docs/Setup.md) | [(English)](Docs/Setup_EN.md)
* [Development of new features](Docs/DEVELOP.md)
* [Interesting examples of use of the models](Docs/Good_Examples.md)
* [*Failed* examples of use of the models](Docs/Wrong_Examples.md)

# Usage

After installation and setup, in any console you can type the `ai` command with a subcommand and its arguments.

some of the available subcommands are: `ask, code, edit, chat`

i.e:

`ai ask "Write a list of 10 names for a medieval fantasy King -t 0.9"`

For more detailed explanations of flags type

`ai -h`

or

`ai <command> -h`

## Temperature suggestions

| Usecase | temperature |
| --- | --- |
| Chatbot | 0.5 |
| Story writing | 0.8 |
| Email parser | 0.3 |
| Summarise test | 0.5 |
| Code generation | 0.8 |
| Code refactoring | 0.2 |

# TODO

* Create command for spell checking and maybe writing improvement using the edit endpoint
* Sort the unsorted examples
* Add more experimental assistants to the chat command
