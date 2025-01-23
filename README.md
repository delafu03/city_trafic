# 1. Create a virtual environment

To create a virtual environment in Python, follow these steps:

1. Open a terminal and navigate to your project directory.
2. (A) Run the following command to create a virtual environment named `.venv`:

   ```bash
   python -m venv .venv
   ```

3. (B) Open the VS Code command palette with `Ctrl+Shift+P` (Windows) or `Cmd+Shift+P` (macOS) and type `Python: Create Environment`: select the `Python: Create Environment` option and choose the `./.venv` option to create a virtual environment in the `.venv` folder.

4. Activate the virtual environment:

   - On Windows:

     ```bash
     .\.venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source .venv/bin/activate
     ```

5. Once activated, you will see the name of the virtual environment in the command line.

6. Navigate to the folder containing the `requirements.txt` file:

   ```bash
   cd path/to/requirements.txt
   ```

7. Install the project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

To deactivate the virtual environment, simply run:

```bash
deactivate
```

Para crear un entorno virtual en Python, sigue estos pasos:

1. Abre una terminal y navega al directorio de tu proyecto.
2. (A) Ejecuta el siguiente comando para crear un entorno virtual llamado `.venv`:

   ```bash
   python -m venv .venv
   ```

3. (B) Abre la paleta de comandos de VS Code con `Ctrl+Shift+P` y escribe `Python: Create Environment`: selecciona la opción `Python: Create Environment` y elige la opción `./.venv` para crear un entorno virtual en la carpeta `.venv`.

4. Activa el entorno virtual:

   - En Windows:

     ```bash
     .\.venv\Scripts\activate
     ```

   - En macOS y Linux:

     ```bash
     source .venv/bin/activate
     ```

5. Una vez activado, verás el nombre del entorno virtual en la línea de comandos.

6. Accede a la carpeta que contiene el archivo `requirements.txt`:

   ```bash
   cd path/to/requirements.txt

   ```

7. Instala las dependencias del proyecto:

   ```bash
   pip install -r requirements.txt
   ```

Para desactivar el entorno virtual, simplemente ejecuta:

```bash
deactivate
```
