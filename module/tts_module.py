from gtts import gTTS
from pydub import AudioSegment
import os

def say(text, lang='id', filename='output/suara.mp3', speed=1.0):
    os.makedirs('output', exist_ok=True)
    temp_file = 'output/temp.mp3'

    try:
        # Buat suara
        tts = gTTS(text=text, lang=lang)
        tts.save(temp_file)

        # Ubah kecepatan
        sound = AudioSegment.from_file(temp_file)
        sound = sound.speedup(playback_speed=speed)
        sound.export(filename, format='mp3')

        # Mainkan
        os.system(f"mpg123 {filename}")

    except Exception as e:
        print("❌ Gagal menjalankan say():", e)
