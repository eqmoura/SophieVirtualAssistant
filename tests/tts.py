import pyttsx3
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

engine.say("xaaaaatooo, está em português")
engine.runAndWait()