# Trinity python client
Cliente con reconocimiento de voz. Funciona solo desde python y no necesita google-chrome.
Posee wake-word (palabra de activacion). En este caso "TRINITY".
Puede funcionar para markopolo con facilidad. Tan solo configurando puertos y password.

## Dependencias:
- libatlas-base-dev
- python3-pyaudio

## Archivos de configuracion:

* python-client/01_hwd_detected.sh        - Script de bash que se ejecuta al detectar la hotword
* python-client/02_stt_result.sh          - Script de bash que se ejecuta al recibir la transcripcion
* python-client/03_srv_response.sh        - Script de bash que se ejecuta al recibir la respuesta.
* python-client/client_config.py          - Define puerto del servidor, usuario, contraseña
* python-client/hotword.pmdl              - link a 'howords/trinity2021.pmdl'. Puede redirijirlo al modelo de markopolo, en la misma carpeta.


## Ejecucion

El cliente puede funcionar en dos modos:

### **1. En modo deamon** 
En esta modalidad el cliente espera una wake-word antes de iniciar el reconocimiento de voz. Y luego de realizar la comunicacion continua escuchando. Ejecute...

      ./run_pyclient.sh             (para iniciar el deamon cliente)
      ./stop_pyclient.sh            (para detener el deamon cliente)

   #### Bloqueo de wake-word
   En ocasiones el reconocimiento de voz suele molestar. Por ejemplo cuando estamos viendo un video.
   Para evitar la activacion de la wake-word basta con crear un archivo vacio. Utilice los siguientes comandos:

      touch /tmp/snowboystop            (para anular la activacion de la wake-word)
      rm /tmp/snowboystop               (para reestablecer el normal funcionamiento)


### **2. En modo disparo único** 
En esta modalidad el cliente activa el reconocimiento de voz y realizar la comunicacion por unica vez. Es util para configurarlo junto a un atajo de teclado, y tambien para utilizarlo en las "answers" del servidor. Ejecute...
            ./pyclient_once.sh             (para iniciar la captura de audio)
