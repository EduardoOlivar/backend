# Backend para proyectos de la universidad
## Daniel Duran - José Olivar - Luis Romero

Para iniciar el backend es necesario recrear ciertos pasos previamente en su IDE.
Primero clonar la repo, luego en la carpeta que se descarga, se abre con el IDE, y tiene escribir los siguientes comandos en la terminal

py -m venv venv

Si usa VSC apretar f1 y escribir "interpreter, escoger la opción Python 3.10.x ('venv':venv), luego cerrar la consola y volver a abrir

Siguiendo este paso escribir el siguiente comando para instalar las depencencias desde el archivo requirements.txt

pip install -r requirements.txt

Luego que se instalen las depencencias, es necesario tener MySQL Workbench para poder crear el esquema de la base de datos.

En settings.py se debe encontrar esta parte

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'proyecto_web',
            'USER': 'root',
            'PASSWORD': '',
            'HOST': 'localhost',
            'PORT': '3306'
        }
    }

Aquí debe incluir la contraseña de su base de datos en la key 'PASSWORD': 'Aquí poner su contraseña', cuando ya se tenga la contraseña, en MySQL Workbench debe crear un schema con este nombre "proyecto_web", al tener creado el esquema, debe ir a su IDE y escribir el siguiente comando

py manage.py migrate

Este comando creara la base de datos con sus tablas a traves del ORM de Django.

Para poblar las tablas de la base de datos es necesario ocupar el siguiente comando.

py manage.py shell < script/main.py

En caso de que se equivoque al poblar la data escribir el siguiente comando, solo borra las tablas de ensayos, preguntas, respuestas, la tabla de usuarios sigue con la data con la que se registraron.

py manage.py shell < script/reset_db.py

Luego de esto escribir el siguiente comando para inicializar el servidor.

py manage.py runserver





