import os
import requests
from dotenv import load_dotenv

load_dotenv()

ZAPI_INSTANCE_ID = os.getenv("ZAPI_INSTANCE_ID")
ZAPI_TOKEN = os.getenv("ZAPI_TOKEN")

ZAPI_BASE_URL = f"https://api.z-api.io/instances/{ZAPI_INSTANCE_ID}/token/{ZAPI_TOKEN}"

def sendMessage(name: str, number: str):
    url = f"{ZAPI_BASE_URL}/send-text" 
    text = f"Olá {name}, tudo bem com você?!"
    payload = {
        "phone": str(number), 
        "message": text
    }
    try:
        response = requests.post(url, json=payload)

        if response.status_code == 200:
            return {
                "status": "success",
                "message": f"Mensagem enviada para {name} ({number})"
            }
        else:
            return {
                "status": "error",
                "message": f"Erro ao enviar para {name} ({number})",
                "details": response.text
            }

    except requests.RequestException as e:  
        return {
            "status": "error",
            "message": "Erro ao conectar com Z-API",
            "details": str(e)  
        }
