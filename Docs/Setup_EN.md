
- [Initial setup](#initial-setup)
  - [Install requirements](#install-requirements)
  - [Activate the API-KEY](#activate-the-api-key)
- [Run scripts from the proyect](#run-scripts-from-the-proyect)
- [The `ai` command](#the-ai-command)


# Initial setup

## Install requirements

This section describes the steps to follow to be able to run the project *locally*.

1. **Create the python virtual environment**

```shell
python -m venv venv
```

- If `python3-venv` is not available, install it:

```shell
sudo apt install python3.10-venv
```

2. **Enter the virtual environment**

```shell
source venv/bin/activate
```

3. **Install the requirements**

```shell
pip install -r requirements.txt
```

## Activate the API-KEY

1. **Open with an editor the file *.bashrc* of the user's home**

(To see the user's home you can run `cd` in any console)

In some place of the file, export the api key:

`export OPENAI_API_KEY=sk-U<...>L`

2. **Save and close the file.**

3. **Reopen all the consoles that are being used for the change to take effect**

# Run scripts from the proyect

Once the steps of the initial setup are completed, follow these steps to be able to run the project.

1. **Navigate to the base of the project**
2. **Activate the project's environment**

```shell
source venv/bin/activate
```

Now you can run any .py file from the project directly.

The main executable of the project is located in `/prompter/app.py`

# The `ai` command

To be able to use this repo from any console, you can *optionally* do this step to add an alias to the command line function.

Assuming that the virtual environment was made in the base of the repository with the name `venv` as specified in the initial setup, you must open the `.bashrc` file of the user's home

to open it you can do

```bash
cd
nano .bashrc
```

or replace `nano` with any text editor.

At the end of the file, add the following lines:

```shell
export PROMPTER_HOME_DIR=/home/amd/Proyects/Prompter
alias ai="$PROMPTER_HOME_DIR/venv/bin/python $PROMPTER_HOME_DIR/prompter/app.py"
```

replacing what is to the right of `PROMPTER_HOME_DIR=` with the path where the repository was cloned.

To check if it worked, open a new console and type `ai echo test` and should repeat the message "test"
