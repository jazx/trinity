#!/usr/bin/env python3

import speech_recognition as sr
import os

def traducir():

	recognizer = sr.Recognizer()
	recognizer.energy_threshold = 300
	mic = sr.Microphone()
	text = ''

	with mic as source:
		recognizer.adjust_for_ambient_noise(source)
		os.system("aplay -q resources/listen.wav")
		print('Recording...')
		audio = recognizer.listen(source)
		try:
			text = recognizer.recognize_google(audio, language='es-AR')
			os.system("aplay -q resources/endlisten.wav")
			#print(text)
		except sr.UnknownValueError:
			print('Say again...')
		except sr.RequestError:
			print('Service offline')

		return text


		


