# Trinity python client
Este es el primer cliente con reconocimiento de voz. Funciona solo desde python.
Posee wake-word (palabra de activacion). En este caso "TRINITY".
Puede funcionar para markopolo con facilidad. Tan solo configurando puertos y password.

## Bloqueo de wake-word
En ocasiones el reconocimiento de voz suele molestar. Por ejemplo cuando estamos viendo un video.
Para evitar la activacion de la wake-word basta con crear un archivo vacio. Utilice el comando:

      touch /tmp/stopsnowboy            (para anular la activacion de la wake-word)
      rm /tmp/stopsnowboy               (para reestablecer el normal funcionamiento)

## Dependencias:
- libatlas-base-dev
- python3-pyaudio

## Archivos de configuracion:

* python-client/01_hwd_detected.sh        - Script de bash que se ejecuta al detectar la hotword
* python-client/02_stt_result.sh          - Script de bash que se ejecuta al recibir la transcripcion
* python-client/03_srv_response.sh        - Script de bash que se ejecuta al recibir la respuesta.
* python-client/client_config.py          - Define puerto del servidor, usuario, contraseña
* python-client/hotword.pmdl              - link a 'howords/trinity2021.pmdl'. Puede redirijirlo al modelo de markopolo, en la misma carpeta.
