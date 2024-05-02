# Pasos de Ejecucion 
## Instalar PipEnv 
Para poder correr este proyecto necesitamos de un ambiente virtual, para ello lo iniciaremos con pipenv, e instalaremos las dependencias contenidas dentro del pipfile
```bash
pip install pipenv
pipenv install
```

En caso de que python este siendo manejado por brew, usar brew en lugar de pip para instalar pipenv

Ahora, procedemos a correr el ambiente virtual
```bash
pipenv shell
```
Ahora que tenemos al ambiente virtual corriendo, el siguiente paso sera seleccionarlo como interprete, ya que de otra manera la instalacion de nuestras dependencias no se vera reflejada

## Configuracion de django
El siguiente paso consiste en instalar toda nuestra configuracion de django, para ello nos moveremos al directorio exam mediante el comando cd y ejecutaremos los comandos makemigrations ym,igrate de la siguiente manera
```bash
cd exam
python manage.py makemigrations
python manage.py migrate 
```
Una vez que se hayan terminado de ejecutar estos comnandos, estamos listos para empezar a correr el servidor de prueba, para ello correremos 
```bash
python manage.py runserver 
```
Django desplegara la actividad del servidor dentro de la terminal de vscode, finalmente, nos queda ejecutar el codigo de encrypcion de la imagen, para ello nos dirigimos al script encrypt.py y cambiamos la linea no. 49 por una ruta absoluta hacia una imagen dentro de su computadora

```python
image_path = '/tu/ruta/aqui/image.jpg'
```

Una vez que se haya echo el cambio, corremos el script, veremos que recibiremos un codigo numero 200 en la terminal de django, indicando que la imagen ha sido subida y decodificada exitosamente, por ultimo, solo nos queda dirigirnos a la url http://localhost:8000/decrypt-image/ y lo que sucedera sera que se descargara la imagen decodificada a nuestro folder de descargas.