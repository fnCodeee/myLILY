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
