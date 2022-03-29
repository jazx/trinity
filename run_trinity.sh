#!/bin/bash

#identifica el directorio donde estan los archivos
basedir=`readlink -e $0 | sed 's:\/[^\/]*$::g'`

echo '--> Iniciando el servidor (trinity)'
bash $basedir/server/run_server.sh &> /dev/null &

echo '--> Iniciando el cliente (trinity)'
bash $basedir/client/python_01/run_pyclient.sh &> /dev/null &

