# 1. Crear un entorno virtual

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
