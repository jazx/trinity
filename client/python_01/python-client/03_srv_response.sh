#!/bin/bash

SRV_RESPONSE=$1

if [  "$1" == ""  ]; then
	notify-send "Trinity" "Cuanto silencio"
else
	notify-send "Trinity" "$SRV_RESPONSE"
fi
