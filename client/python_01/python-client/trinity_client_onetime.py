#!/usr/bin/env python3

from sr import *
import urllib.request 
from client_config import *
import os


def first_corrections(ingreso):

	#vocales minusculas con tilde
	ingreso = ingreso.replace('á','a')
	ingreso = ingreso.replace('é','e')
	ingreso = ingreso.replace('í','i')
	ingreso = ingreso.replace('ó','o')
	ingreso = ingreso.replace('ú','u')

	return ingreso

os.system("touch /tmp/snowboystop")

texto = traducir()
os.system("bash 02_stt_result.sh '"+texto+"'")
print('Result: '+texto)

#preparando variables
txtinput = first_corrections(texto)
comando = txtinput.replace(' ', '+')
puerto = str(port_srv)

laurl = "http://localhost:"+puerto+"/PSW_"+password_srv+"_PSWUSR_"+user_client+"_USRCOM_@"+comando+"_COM"
#comreq = urllib.request.urlopen(laurl)

comreq = ''
respuesta = 'Trinity Server Error'

try:
	if comando == '' :
		print('No string to send.')
	else:
		print('Sending get request...')
		comreq = urllib.request.urlopen(laurl)
		trinityresponse = comreq.read()
		
		respuesta = str(trinityresponse)
		respuesta = respuesta.replace("b'", '')
		respuesta = respuesta.replace("\'", '')
		
		os.system("bash 03_srv_response.sh '" + respuesta + "'")
		
except:
	os.system("bash 03_srv_response.sh 'Trinity Server Error'")
	pass


os.system("rm /tmp/snowboystop")