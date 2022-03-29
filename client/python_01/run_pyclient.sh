#!/bin/bash

#identifica el directorio donde estan los archivos
basedir=`readlink -e $0 | sed 's:\/[^\/]*$::g'`

echo '  > Server python para Trinity Client'
cd $basedir/python-client
./bin/python3 goclient.py
