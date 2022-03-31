#!/bin/bash

#identifica el directorio donde estan los archivos
basedir=`readlink -e $0 | sed 's:\/[^\/]*$::g'`

echo '--> Ejecutando el cliente python (trinity)'
cd $basedir/python-client
./bin/python3 trinity_client_onetime.py
cd $basedir
