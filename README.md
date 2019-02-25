# Karl - Notificaciones genéricas vía Telegram

**Karl**, que toma su nombre de [Karl Malone](https://es.wikipedia.org/wiki/Karl_Malone), jugador de la NBA y apodado *"El cartero"*, es un sistema hecho en Python para notificar a canales propios vía Telegram.

![Karl Malone](karl-malone.jpg)

## Uso

- Crear el fichero `.env` con los valores que correspondan.
- Crear el fichero `groups.dat` con `clave = valor` donde *clave* es el nombre del grupo y *valor* es el identificador *Telegram*.

~~~console
$ pipenv install
$ flask run
~~~

## Ejemplo de llamada

~~~python
>>> import requests
>>> requests.post('http://<domain>:<port>/api/send_message', data={'msg': 'Un mensaje de prueba', 'groups': 'dev', 'token': '<auth_token>'})
~~~

> Esta solicitud enviaría el mensaje *"Un mensaje de prueba"* al grupo *"dev"* utilizando el token de autenticación *<auth_token>*.
