#!/usr/bin/env python3

import dicc
import dicc2
import brodmann_four
import re
import sys
import os
import subprocess

def procesar (ingreso,user):
	
	#ponemos todo en minusculas
	ingreso = ingreso.lower()
	
	tags = dicc.tagcreator(ingreso)
	
	#aislando nombre de sector
	sector = re.sub('.*<', '', tags)
	sector = re.sub('>.*', '', sector)
	
	#define el path del segundo diccionario
	dicc2path = 'sectors/'+sector
	
	print("Recived: %s" % ingreso)
	print("User: %s" % user)

	
	if (os.path.isdir(dicc2path) == True):
		# importa el diccionario secundario desde el directorio del sector
		#sys.path.append(dicc2path)
		#import dicc2
		
		# define las tags desde el diccionario secundario
		finaltags = dicc2.tagcreatortwo(ingreso,dicc2path)

		print("Sector: %s" % sector)
		print("Tags: %s" % finaltags)
		
		salida = brodmann_four.ejecutar(finaltags,ingreso,user,dicc2path)
		
	else:
		print("Sector: "+sector+" [error: folder not found]")
		tagsexec_args = 'sectors/+NOSECTOR+'+' '+user+' '+ingreso
		outputcomando = subprocess.run(tagsexec_args, stdout=subprocess.PIPE, shell=True)
		resultado = outputcomando.stdout	
		print('Exec:',tagsexec_args)
		print(' >>>:',resultado)
		salida = resultado
			

	print('')
	
	return salida
