# Sistema de Registro de Cedulas + API REST con FAST API y MYSQL

Instalacion del Back End de manera local y sencilla.

Por favor, a la hora de crear la cedula, si gusta probar creala con la siguiente estructura 2-0000-0000
Esto con el fin de que no se genere errores o bugs inesperados con el bot de discord.

1. Descargar o Clona el repositorio en tu computadora.
2. Abre Visual Studio Code y carga la carpeta del proyecto.
3. Abre la terminal integrada con Ctrl + ñ o Terminal > New Terminal.
4. Crear un entorno virtual (opcional pero recomendado):
Ejecuta el entorno virtual aplicando el paso 3 + esta linea de codigo: python -m venv venv

5. Activar el entorno virtual:
* En Windows. venv\Scripts\activate
* En Linux/Mac. source venv/bin/activate

6. Instalar las dependencias:
pip install -r requirements.txt

7. Ejecutar el backend:
uvicorn app.main:app --reload

8. Abrir en el navegador:
Puedes escribir esto en tu navegado: http://127.0.0.1:8000/docs
O puedes dar Control + click izquiero en el link que sale en la consola de VS Code.


Endpoints disponibles
Método          Endpoint            Descripción
GET	            /usuarios	        Listar todos los usuarios
GET	            /usuarios/{cedula}  Consultar usuario por cédula
POST	        /usuarios	        Registrar nuevo usuario
PUT	            /usuarios/{cedula}	Actualizar usuario por cédula
DELETE	        /usuarios/{cedula}	Eliminar usuario por cédula

Ejemplo de Uso:

Obtener un usuario
GET /usuarios/1-0000-0001
Respuesta Esperada.
{"nombre":"Sebastian","apellido":"Basteri","nacionalidad":"Costarricense","estatura":"180","fecha_nacimiento":"04/04/2005","edad":"20","sexo":"Hombre","usuario_discord":389484160269549570,"usuario_roblox":"justinpadilla885","id":2,"cedula":"1-0000-0001"}


