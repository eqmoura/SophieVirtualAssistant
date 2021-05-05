#Our main file

import speech_recognition as sr

#Cria um reconhecedor
r = sr.Recognizer()

#Abrir o microfone
with sr.Microphone() as source:
    while True:
        audio = r.listen(source)#Define o microfone como fonte de audio
        print(r.recognize_google(audio))
#Saindo pra trabalhar 9:05, as 19h estou de volta para tentar mais coisas