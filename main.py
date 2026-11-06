from fastapi import FastAPI
import database

app = FastAPI(title="Tenk It Backend API")

# 1. Ana Sayfa Adresi (Test)
@app.get("/")
def ana_sayfa():
    return {"mesaj": "Tenk It Backend API Sunucusu Çalışıyor!"}

# 2. Konuları Listeleyen Adres
@app.get("/topics")
def konulari_listele():
    konular = database.tum_konulari_getir()
    return {"status": "success", "data": konular}

# 3. Yeni Konu Ekleyen Adres
@app.post("/topics")
def yeni_konu(title: str, category: str):
    eklenen = database.konu_ekle(title, category)
    return {"status": "success", "data": eklenen}

# 4. Tüm Tenk'leri Listeleyen Adres
@app.get("/tenks")
def tenkleri_listele():
    tenkler = database.tum_tenkleri_getir()
    return {"status": "success", "data": tenkler}

# 5. Yeni Tenk (Eleştiri) Ekleyen Adres
@app.post("/tenks")
def yeni_tenk(user_id: str, topic_id: str, content: str, sentiment_type: str):
    eklenen = database.tenk_ekle(user_id, topic_id, content, sentiment_type)
    return {"status": "success", "data": eklenen}

# 6. Oy / Etkileşim Ekleyen Adres
@app.post("/interactions")
def yeni_etkilesim(user_id: str, tenk_id: str, interaction_type: str):
    eklenen = database.etkilesim_ekle(user_id, tenk_id, interaction_type)
    return {"status": "success", "data": eklenen}