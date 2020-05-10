from gtts import gTTS
from playsound import playsound

x = input('Enter: ')


a = gTTS(x)
a.save("Google Text To Speech.mp3")

playsound("Google Text To Speech.mp3")
