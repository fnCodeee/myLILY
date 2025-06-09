import speech_recognition as sr

def listen_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Kalibrasi noice...")
        r.adjust_for_ambient_noise(source, duration=1.2)

        print("Say anything...")
        audio = r.listen(source)

    try: 
        text = r.recognize_google(audio, language="id-ID")
        print("Says: ", text)
        return text
    except sr.UnknownValueError:
        print("Maaf suara tidak dikenali!")
        return None
    except sr.RequestError as e:
        print(f"Gagal koneksi ke layanan Google Speech: {e}")
        return None