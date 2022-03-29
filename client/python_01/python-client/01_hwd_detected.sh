#!/bin/bash
basedir=`readlink -e $0 | sed 's:\/[^\/]*$::g'`
aplay -q `ls $basedir/voice/* | shuf -n 1` &

