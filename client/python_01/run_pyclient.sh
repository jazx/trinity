#!/bin/bash

#identifica el directorio donde estan los archivos
basedir=`readlink -e $0 | sed 's:\/[^\/]*$::g'`

echo '  > Cliente python para Trinity'

echo '--> Iniciando el client python (trinity)'
cd $basedir/python-client
# borrando lock de snowboy
rm /tmp/snowboystop 2> /dev/null
screen -c ./screen_conf -S trinity_python_client -d -m ./bin/python3 trinity_client.py
