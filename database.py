from supabase import create_client, Client

SUPABASE_URL = "https://xkruaxtxdzmoynvkwzhz.supabase.co"
SUPABASE_KEY = "sb_secret_ILLf7agYI1Zk4B51gaaUqQ_oo-v_mcy"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


# Tüm konuları getiren fonksiyon
def tum_konulari_getir():
    res = supabase.table('topics').select("*").execute()
    return res.data


# Yeni konu ekleyen fonksiyon
def konu_ekle(baslik: str, kategori: str):
    data = {"title": baslik, "category": kategori}
    res = supabase.table('topics').insert(data).execute()
    return res.data


# Tüm tenkleri getiren fonksiyon
def tum_tenkleri_getir():
    res = supabase.table('tenks').select("*, profiles(username), topics(title)").execute()
    return res.data


# Yeni Tenk (eleştiri) ekleyen fonksiyon
def tenk_ekle(user_id: str, topic_id: str, icerik: str, duygu_durumu: str):
    data = {
        "user_id": user_id,
        "topic_id": topic_id,
        "content": icerik,
        "sentiment_type": duygu_durumu
    }
    res = supabase.table('tenks').insert(data).execute()
    return res.data


# Eleştiriye oy veren fonksiyon (interactions tablosu)
def etkilesim_ekle(user_id: str, tenk_id: str, type_val: str):
    # interactions tablosundaki sütun yapısına uygun gönderim
    data = {
        "user_id": user_id,
        "tenk_id": tenk_id
    }
    res = supabase.table('interactions').insert(data).execute()
    return res.data


