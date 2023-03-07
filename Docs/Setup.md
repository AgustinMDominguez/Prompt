
- [Setup inicial](#setup-inicial)
  - [Instalar los requisitos](#instalar-los-requisitos)
  - [Activar la API-KEY](#activar-la-api-key)
- [Iniciar el entorno](#iniciar-el-entorno)
- [El comando `ai`](#el-comando-ai)


# Setup inicial

## Instalar los requisitos

1. **Crear el entorno virtual de Python**

`python -m venv venv`

- Si `python3-venv` no está disponible, instalarlo:

`sudo apt install python3.10-venv`

2. **Entrar en el entorno virtual**

`source venv/bin/activate`

3. **Instalar los requirements**

`pip install -r requirements.txt`

## Activar la API-KEY

1. **Abrir con un editor el archivo *.bashrc* de la home del usuario**

(Para ver la home del usuario se puede correr `cd` en cualquier consola)

En algun lugar del archivo, exportar la api key:

`export OPENAI_API_KEY=sk-U<...>L`

2. **Guardar y cerrar el archivo.**

3. **Reabrir todas las consolas que se están usando para que el cambio surta efecto**

# Iniciar el entorno

1. **Navegar a la base del proyecto**
2. **Activar el entorno del proyecto**

`source venv/bin/activate`

Ahora se puede correr directamente cualquier archivo .py del proyecto.

El archivo ejecutable principal del proyecto se encuentra en `/prompter/app.py`

# El comando `ai`

Para poder usar este repo desde cualquier consola se puede hacer este paso *opcional* para agregar un alias al script principal.

Suponiendo que se hizo el entorno virtual en la base del repositorio con el nombre `venv` como se especifica en el setup inicial, se debe abrer el archivo `.bashrc` de la home del usuario

para abrirla se puede hacer

```bash
cd
nano .bashrc
```

o reemplazando `nano` por cualquier editor de texto.

Luego al final del archivo agregar las siguientes lineas:

```shell
export PROMPTER_HOME_DIR=/home/amd/Proyects/Prompter
alias ai="$PROMPTER_HOME_DIR/venv/bin/python $PROMPTER_HOME_DIR/prompter/app.py"
```

reemplazando lo que está a la derecha de `PROMPTER_HOME_DIR=` por el path a donde fue clonado el repositorio.

Luego para comprobar que funcionó, abrir una consola nueva y tipear `ai echo test` y deberia repetir el mensaje "test"