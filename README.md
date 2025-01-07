# backend-test
Presentacion prueba de backend.

Pasos para la ejecución del proyecto en maquinas con Windows:
1. Instalar Python version 3.12.5
2. Comprobar que la version de python este instalada correctamente ejecutando el comando en el cmd: python --version.
3. Instalar la libreria de python virtual environment con el comando en el cmd: pip install virtualenv
4. Comprobar que virtual environment este instalado correctamente utilizando el comando: pip list y verificando que este la libreria virtualenv instalada.
5. Clonar el repositorio.
6. Ejecutar el comando "python -m venv venv" dentro de la carpeta del repositorio.
7. Activar el entorno virtual navegando en el cmd a la siguiente ruta "venv > Scripts" y  ejecutar "activate".
8. Verificar que el entorno virtual se este ejecutando correctamente (Se indica con unos parentesis al inicio de cada linea de comando).
9. Navegar nuevamente hasta la carpeta raiz en donde se encuentra la carpeta "venv".
10. Ejecutar el comando "pip install -r requirements.txt" para instalar las dependencias necesarias.
11. Ejecutar el comando "python manage.py makemigrations" para realizar las migraciones correspondientes.
12. Ejecutar el comando "python manage.py migrate" para crear las migraciones correspondientes.
13. Ejecutar el comando "python manage.py runserver" para ejecutar el servidor que contiene la solucion de la prueba.
14. Probar los dos diferentes endpoints entregados en la coleccion de Postman que se encuentran en el repositorio.
