import os
import sys

# Bungkam error ALSA dan JACK
sys.stderr = open(os.devnull, 'w')
os.environ['SDL_AUDIODRIVER'] = 'dsp'     # atau 'dummy' kalau ga ada soundcard
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "1"
os.environ['ALSA_CARD'] = 'default'
os.environ['AUDIODEV'] = 'null'
os.environ['JACK_NO_START_SERVER'] = '1'

from module.tts_module import say
from module.ai_module import get_ollama_chat_completion
from module.stt_module import listen_speech
    
if __name__ == "__main__":
    print("mulai mendengarkan (tekan Ctrl + C untuk keluar)!")

    status = False
    while True:
        try:
            # user_input = listen_speech()
            user_input = input("input:\n")
            if user_input is None:
                print("Hah ngomong apa? coba ulangin..")
                continue

            user_input = user_input.lower()

            trigger_keywords = ['Lily', 'lita', 'lili']
            if any(keyword in user_input.lower() for keyword in trigger_keywords):
                status = True
                say("Iya sayanghh, ada yang bisa aku bantu?", speed=1.2)
                continue

            elif "aku pergi dulu" in user_input:
                status = False
                say("Yaudah atuu, Sampai nanti!", speed=1.1)
                continue

            elif status:
                reply = get_ollama_chat_completion(user_input)
                print("AI:\n", reply)
                say(reply, speed=1.2)

            else:
                print("Model Nonaktif!!")
                # say("Hahhhhhhhhhh", speed=1.1)
                # os.system(f"mpg123 output/mas_wamas.mp3")

        except:
            print("\nProgam dihentikan.")
            break

    