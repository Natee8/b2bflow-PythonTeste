from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()

SUPABASEURL = os.getenv('SUPABASE_URL')
SUPABASEKEY = os.getenv('SUPABASE_KEY')

supabase = create_client(SUPABASEURL, SUPABASEKEY)

def searchContacts():
    response = supabase.table('Peoples').select("name, phone").execute()
    return response.data if response.data else []
