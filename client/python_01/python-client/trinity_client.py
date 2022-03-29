#!/usr/bin/env python3

import snowboydecoder
from sr import *
import os
import urllib.request
from client_config import *


def first_corrections(ingreso):

	#vocales minusculas con tilde
	ingreso = ingreso.replace('á','a')
	ingreso = ingreso.replace('é','e')
	ingreso = ingreso.replace('í','i')
	ingreso = ingreso.replace('ó','o')
	ingreso = ingreso.replace('ú','u')

	return ingreso


def comunication_cli_srv():
	texto = traducir()
	os.system("bash 02_stt_result.sh '"+texto+"'")
	print('Result: '+texto)
	print('Send to server...')

	#preparando variables
	txtinput = first_corrections(texto)
	comando = txtinput.replace(' ', '+')
	puerto = str(port_srv)

	laurl = "http://localhost:"+puerto+"/PSW_"+password_srv+"_PSWUSR_"+user_client+"_USRCOM_@"+comando+"_COM"
	#comreq = urllib.request.urlopen(laurl)
	
	comreq = ''
	trinityresponse = 'Trinity Server Error'
	
	try:
		comreq = urllib.request.urlopen(laurl)
		trinityresponse = comreq.read()
	except:
		pass	
	
	respuesta = str(trinityresponse)
	respuesta = respuesta.replace("b'", '')
	respuesta = respuesta.replace("\'", '')
	
	print("Server Response: "+respuesta)
	os.system("bash 03_srv_response.sh '" + respuesta + "'")




def detected_callback():
	print ("Hotword Detected!")
	
	tfile = os.path.exists('/tmp/snowboystop')
	if tfile == False:
		print('Initializing speech recognition...')
		comunication_cli_srv()
	else:
		print('Speech recognition locked... remove /tmp/snowboystop to unlock')
	
	
	


#detector = snowboydecoder.HotwordDetector("hotword.pmdl", sensitivity=0.5, audio_gain=1)
detector = snowboydecoder.HotwordDetector("hotword.pmdl", sensitivity=0.47, audio_gain=1)

detector.start(detected_callback)
