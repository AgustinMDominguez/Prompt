
- [Setup inicial](#setup-inicial)
  - [Instalar los requisitos](#instalar-los-requisitos)
  - [Activar la API-KEY](#activar-la-api-key)
- [Iniciar el entorno](#iniciar-el-entorno)


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

1. **Abrir con un editor el archivo *.bashrc* de la home**

En algun lugar del archivo, exportar la api key:

`export OPENAI_API_KEY=sk-U<...>L`

2. **Guardar y cerrar el archivo.**

3. **Reabrir todas las consolas que se están usando para que el cambio surta efecto**

# Iniciar el entorno

1. **Navegar a la base del proyecto**
2. **Activar el entorno del proyecto**

`source venv/bin/activate`
