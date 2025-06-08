import speech_recognition as sr

r = sr.Recognizer()

while True:
    with sr.Microphone() as source:
        print("kalibrasi noice latarbelakang")
        r.adjust_for_ambient_noise(source, duration=0.8)

        print("Ucapkan sesuatu...")
        audio = r.listen(source)    

    try:
        text = r.recognize_google(audio, language=("id-ID"))
        print("Kamu bilang:\n", text, "\n\n")
    except sr.UnknownValueError: 
        print("Tidak bisa Mengenali Suara")
    except sr.RequestError as e:
        print("Gagal konek ke layanan google speech: {0}".format(e))