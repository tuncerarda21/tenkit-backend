import os
from supabase import create_client, Client

url: str = "https://xkruaxtxdzmoynvkwzhz.supabase.co"
key: str = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(url, key)

