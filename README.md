This is a personal space for testing and developing Proofs of Concept for Application of the Open AI API.

Para probar la API en caliente sin tener que corre constantemente los mismos pedidos, mejor usar un notebook de Jupyter: Ver el archivo [`workshop.ipynb`](src/workshop.ipynb)

# Links

* [Commits Documentation](Docs/Commits.md)
* [Instalación y setup](Docs/Setup.md)

# Tips

### Sugerencia de Temperatura

| Usecase | temperature |
| --- | --- |
| Chatbot | 0.5 |
| Store writing | 0.8 |
| Email parser | 0.3 |
| Summarise test | 0.5 |
| Code generation | 0.8 |
| Code refactoring | 0.2 |

`pycodestyle . --exclude=venv/*,**ignore* --max-line-length=100`

# TODO

* Create DEVELOP.md for developing tips and move the pycodestyle instruction
* Create command for spell checking and maybe writing improvement using the edit endpoint
* Sort the unsorted examples
* Add further explanation on how to create the "ai" console command
* Add echo command help
* Add the missing help strings
