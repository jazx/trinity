#!/bin/bash

echo '--> Cerrando WebClient (browser)'
kill `ps aux | grep 'chrome --app=http://localhost:9091/index.html' | grep -v grep | awk '{print $2}'` 2> /dev/null

echo '--> Cerrando WebClient (pyserver)'
kill `ps aux | grep 'SCREEN -c ./screen_conf -S trinity_webclient -d -m python3 -m http.server 9091' | grep -v grep | awk '{print $2}'` 2> /dev/null

