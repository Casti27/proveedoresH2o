# clientes/utils.py
import requests

def obtener_ngrok_url():
    try:
        res = requests.get("http://127.0.0.1:4040/api/tunnels")
        if res.status_code == 200:
            data = res.json()
            for tunel in data["tunnels"]:
                if tunel["proto"] == "https":
                    return tunel["public_url"]
    except requests.exceptions.RequestException:
        pass
    return "http://localhost:8000"  # Fallback si ngrok no está activo
