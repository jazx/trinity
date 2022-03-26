#!/bin/bash

#identifica el directorio donde estan los archivos
basedir=`readlink -e $0 | sed 's:\/[^\/]*$::g'`

echo '--> Estableciendo nuevo PATH'
PATH=$PATH:$basedir/server/bin

echo '--> Iniciando el servidor Brain (trinity)'
cd $basedir/server/brain
screen -c ../config/screen_conf -S trinity_brain -d -m ./trinity.py


echo '--> Reproduciendo saludo'
trinity-randomwav init 2> /dev/null &
