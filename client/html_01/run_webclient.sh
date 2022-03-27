#!/bin/bash

#identifica el directorio donde estan los archivos
basedir=`readlink -e $0 | sed 's:\/[^\/]*$::g'`

echo '  > Server python para Trinity Client'
cd $basedir/webclient
#ejecuta el servidor
screen -c ./screen_conf -S trinity_webclient -d -m python3 -m http.server 9091

echo '  > Borrando la cache del navegador'
rm -Rf /home/$USER/.cache/google-chrome


echo '  > Abriendo navegador Google Chrome'
google-chrome --app=http://localhost:9091/index.html 2&> /dev/null &
while [ -z "`wmctrl -l | grep 'Trinity Client'`" ];do echo -n "." ; sleep 0.15 ; done ; echo '.'

echo '  > Ubicando ventana'
wmctrl -R 'Trinity Client' -e 0,1400,100,400,250 
