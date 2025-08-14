from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_KEY')

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("Credenciais do Supabase não encontradas no .env")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def searchContacts():
    try:
        response = supabase.table('Peoples').select("name, phone").execute()
        return response.data if response.data else []
    except Exception as e:
        return {
            "status": "error",
            "message": "Erro ao buscar contatos no Supabase",
            "details": str(e)
        }
