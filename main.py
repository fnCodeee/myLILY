import os
import sys

# Bungkam error ALSA dan JACK
sys.stderr = open(os.devnull, 'w')

from tts_module import say
from ai_module import get_ollama_chat_completion
from stt_module import listen_speech
    
if __name__ == "__main__":
    print("mulai mendengarkan (tekan Ctrl + C untuk keluar)!")

    status = False
    while True:
        try:
            user_input = listen_speech()
            # user_input = input("input:\n")
            if user_input is None:
                print("Hah ngomong apa? coba ulangin..")
                continue

            user_input = user_input.lower()

            if "halo lily" in user_input or "halo lili" in user_input:
                status = True
                say("Iya Faiz, ada yang bisa aku bantu?")
                continue

            elif "tidur sana" in user_input:
                status = False
                say("Yaudah atuu, Sampai nanti iz!")
                continue

            elif status:
                reply = get_ollama_chat_completion(user_input)
                print("AI:\n", reply)
                say(reply)

            else:
                print("Model Nonaktif!!")

        except:
            print("\nProgam dihentikan.")
            break

    