# 🤖 LILY - AI Assistant with Local Ollama Model

LILY adalah asisten AI berbasis suara yang berjalan **sepenuhnya lokal** menggunakan [Ollama](https://ollama.com). Dibekali dengan Google Text-to-Speech dan SpeechRecognition, LILY dapat mendengarkan suara pengguna, merespon dengan AI lokal (seperti LLaMA3), dan membalas dalam bentuk suara.

---

## ✨ Fitur

- 🎤 Input suara menggunakan microphone
- 🧠 Pemrosesan prompt oleh AI lokal (Ollama)
- 🔊 Output suara via Google TTS
- 🖥️ Support untuk **Linux**, **Windows**, dan **macOS**

---

## 🛠️ Teknologi

- **Bahasa:** Python 3
- **Speech-to-Text:** `SpeechRecognition`, `PyAudio`
- **Text-to-Speech:** `gTTS`, `pydub`
- **Model AI:** `Ollama` (LLaMA3 atau model lainnya)
- **Platform Support:** ✅ Windows / ✅ macOS / ✅ Linux

---

## 📥 Instalasi

### 🐧 Linux (Debian/Ubuntu)

```bash
# Install dependency sistem
sudo apt update
sudo apt install python3 python3-pip portaudio19-dev ffmpeg -y

# Clone repositori
git clone https://github.com/username/lily-ai.git
cd lily-ai

# Buat dan aktifkan virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependency Python
pip install -r requirements.txt

# Jalankan Ollama dan model (pastikan Ollama sudah terinstall)
ollama run llama3
```


##
🪟 Windows (CMD / PowerShell)

```bash
# Clone repositori
git clone https://github.com/username/lily-ai.git
cd lily-ai

# Buat virtual environment
python -m venv venv

# Aktifkan virtual environment (pilih salah satu tergantung terminal)
venv\Scripts\activate.bat      # Jika pakai CMD
venv\Scripts\Activate.ps1      # Jika pakai PowerShell

# Install pipwin dan PyAudio (solusi untuk error pyaudio)
pip install pipwin
pipwin install pyaudio

# Install semua dependensi Python
pip install -r requirements.txt

# Jalankan model AI lokal
ollama run llama3
```


📌 Jika Activate.ps1 diblokir oleh PowerShell, jalankan perintah ini terlebih dahulu:

```bash
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

##
🍎 macOS

```bash
# Install Homebrew jika belum (untuk ffmpeg & portaudio)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install dependency sistem
brew install ffmpeg portaudio

# Clone repositori
git clone https://github.com/username/lily-ai.git
cd lily-ai

# Buat dan aktifkan virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependensi Python
pip install -r requirements.txt

# Jalankan model AI lokal
ollama run llama3
```
