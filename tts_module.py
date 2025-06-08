from gtts import gTTS
import os

# Test ganti ke suara
# text = "Hallo Faiz, Gimana kabarmu"
# tts = gTTS(text=text, lang='id')
# tts.save("output/suara.mp3")
# os.system("mpg123 output/suara.mp3")

def say(text, lang='id', filename='output/suara.mp3'):
    tts = gTTS(text=text, lang=lang)
    tts.save(filename)
    os.system(f"mpg123 {filename}")