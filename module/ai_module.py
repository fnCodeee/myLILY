import requests

def get_ollama_chat_completion(message_from_user: str) -> str:
    url = "http://localhost:11434/api/chat" # url local ollama
    headers = {"Content-Type": "application/json"}
    
    payload = {
        "model": "lilyV2-gm1b", #gunakan model yang sudah di pull ke local ollama
        "messages": [
            {
                "role": "user",
                "content": message_from_user
            }
        ],
        "stream": False
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data["message"]["content"]
    except Exception as e: 
        print("Error saat memanggil ollama API:", e)
        return "Maaf, AI sedang sibuk. Jangan sok asik."
