from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from ytmusicapi import YTMusic
import uvicorn
import os

app = FastAPI(title="Web Music API", version="2.3.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize YTMusic
ytmusic = YTMusic()

# ============== HOME ENDPOINTS ==============

@app.get("/api/home")
async def get_home_content():
    """Get home page content"""
    try:
        # Get various content for home page
        charts = ytmusic.get_charts(country="ID")
        
        return {
            "sections": [
                {
                    "id": "sering_dengarkan",
                    "title": "Sering kamu dengarkan",
                    "type": "horizontal",
                    "items": [
                        {"id": "1", "title": "Satu Rasa Cinta", "artist": "Arief", "thumbnail": "https://i.ytimg.com/vi/6nJ1C1kN3sE/hqdefault.jpg"},
                        {"id": "2", "title": "TABOLA BALE", "artist": "SILET OPEN UP", "thumbnail": "https://i.ytimg.com/vi/7Jz9vG8k5sQ/hqdefault.jpg"},
                        {"id": "3", "title": "KUMPULAN LAGU POP KARO ENAK DIDENGAR", "artist": "Narta Siregar", "thumbnail": "https://i.ytimg.com/vi/8Kz9vG8k5sQ/hqdefault.jpg"},
                        {"id": "4", "title": "Bahagia Lagi", "artist": "Piche Kota", "thumbnail": "https://i.ytimg.com/vi/9Lz9vG8k5sQ/hqdefault.jpg"},
                    ]
                },
                {
                    "id": "rilis_anyar",
                    "title": "Rilis Anyar (Baru Rilis)",
                    "type": "grid",
                    "items": [
                        {"id": "5", "title": "Tanpa Cinta", "artist": "Yovie Widianto", "thumbnail": "https://i.ytimg.com/vi/MPJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "6", "title": "Merayu Tuhan (feat. Dodhy Kangen)", "artist": "Tri Suaka", "thumbnail": "https://i.ytimg.com/vi/QQJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "7", "title": "Kita Usahakan Lagi", "artist": "Batas Senja", "thumbnail": "https://i.ytimg.com/vi/RRJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "8", "title": "LET ME DEFEAT - Indonesian Pop Songs 2025", "artist": "Teras Entertaiment", "thumbnail": "https://i.ytimg.com/vi/SRJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "9", "title": "Tunggal Eka", "artist": "Denny Caknan", "thumbnail": "https://i.ytimg.com/vi/TRJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "10", "title": "Dan...", "artist": "Sheila On 7", "thumbnail": "https://i.ytimg.com/vi/URJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "11", "title": "Goodbye Lover - Indonesian Pop Songs 2025", "artist": "Teras Entertaiment", "thumbnail": "https://i.ytimg.com/vi/VRJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "12", "title": "Tunggu Saja", "artist": "Radja", "thumbnail": "https://i.ytimg.com/vi/WRJ4x1wY4n0/hqdefault.jpg"},
                    ]
                },
                {
                    "id": "gembira_semangat",
                    "title": "Gembira & Semangat",
                    "type": "grid",
                    "items": [
                        {"id": "13", "title": "Tetap Semangat", "artist": "Bondan Prakoso", "thumbnail": "https://i.ytimg.com/vi/XSJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "14", "title": "Ayo Semangat (Pasti Bisa)", "artist": "Nada Swara Gembira", "thumbnail": "https://i.ytimg.com/vi/YSJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "15", "title": "Hati Gembira - Instrumental Version", "artist": "Tentang Anak", "thumbnail": "https://i.ytimg.com/vi/ZSJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "16", "title": "Gembira Adalah Obat", "artist": "Tony Q Rastafara", "thumbnail": "https://i.ytimg.com/vi/aTJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "17", "title": "Da Natiniptip Sanggar", "artist": "Maxima", "thumbnail": "https://i.ytimg.com/vi/bTJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "18", "title": "Semenjak Ada Dirimu", "artist": "Yovie Widianto", "thumbnail": "https://i.ytimg.com/vi/cTJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "19", "title": "Happy Music", "artist": "Nusantarian Dub", "thumbnail": "https://i.ytimg.com/vi/dTJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "20", "title": "Pagi Semangat! - Lagu Anak Ceria", "artist": "Lagu Anak Indonesia", "thumbnail": "https://i.ytimg.com/vi/eTJ4x1wY4n0/hqdefault.jpg"},
                    ]
                },
                {
                    "id": "tangga_lagu",
                    "title": "Tangga Lagu Populer",
                    "type": "grid",
                    "items": [
                        {"id": "21", "title": "Zen Meditation Music, Nature Sounds", "artist": "Nature Sounds", "thumbnail": "https://i.ytimg.com/vi/fTJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "22", "title": "Hours Relaxing Guitar Music", "artist": "Nature Sounds", "thumbnail": "https://i.ytimg.com/vi/gTJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "23", "title": "Coffee Shop Music - Relax Jazz Cafe", "artist": "Relaxing Piano Life", "thumbnail": "https://i.ytimg.com/vi/hTJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "24", "title": "BEST GUITAR ROMANTIC INSTRUMENTAL", "artist": "Acoustic Guitar Music", "thumbnail": "https://i.ytimg.com/vi/iTJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "25", "title": "Somebody's Pleasure", "artist": "Aziz Hedra", "thumbnail": "https://i.ytimg.com/vi/jTJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "26", "title": "Teenage Senorita Medley", "artist": "Victor Wood", "thumbnail": "https://i.ytimg.com/vi/kTJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "27", "title": "Dandelions", "artist": "Ruth B.", "thumbnail": "https://i.ytimg.com/vi/lTJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "28", "title": "R.I.O. Megamix (Continuous DJ Mix)", "artist": "R.I.O.", "thumbnail": "https://i.ytimg.com/vi/mTJ4x1wY4n0/hqdefault.jpg"},
                    ]
                },
                {
                    "id": "galau_terpopuler",
                    "title": "Galau Terpopuler",
                    "type": "grid",
                    "items": [
                        {"id": "29", "title": "Bertahan Sakit Pergi Sulit", "artist": "Syahriyadi", "thumbnail": "https://i.ytimg.com/vi/nTJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "30", "title": "Lumpuhkan Ingatanku", "artist": "Geisha", "thumbnail": "https://i.ytimg.com/vi/oTJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "31", "title": "Kenangan Terindah", "artist": "SAMSONS", "thumbnail": "https://i.ytimg.com/vi/pTJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "32", "title": "Jiwa Yang Bersedih", "artist": "Ghea Indrawari", "thumbnail": "https://i.ytimg.com/vi/qTJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "33", "title": "bergema sampai selamanya", "artist": "Nadhif Basalamah", "thumbnail": "https://i.ytimg.com/vi/rTJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "34", "title": "Menua Bersamamu", "artist": "Shandy Pagalla Channel", "thumbnail": "https://i.ytimg.com/vi/sTJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "35", "title": "Tak Ingin Usai", "artist": "Keisya Levronka", "thumbnail": "https://i.ytimg.com/vi/tTJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "36", "title": "Mati-Matian", "artist": "Mahalini", "thumbnail": "https://i.ytimg.com/vi/uTJ4x1wY4n0/hqdefault.jpg"},
                    ]
                },
                {
                    "id": "baru_diputar",
                    "title": "Baru diputar",
                    "type": "grid",
                    "items": [
                        {"id": "37", "title": "Cinta Merah Jambu (feat. Ajeng)", "artist": "LEK PANG", "thumbnail": "https://i.ytimg.com/vi/vTJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "38", "title": "Aku Dah Lupa", "artist": "Maman Fvndy", "thumbnail": "https://i.ytimg.com/vi/wTJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "39", "title": "Asmara Kerinduan (Remix)", "artist": "Meyda Rahma", "thumbnail": "https://i.ytimg.com/vi/xTJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "40", "title": "KUAN SOE LEKONES (COVER TERBARU 2026)", "artist": "AITINA MUSIK", "thumbnail": "https://i.ytimg.com/vi/yTJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "41", "title": "Tabola Bale x Lampu Kaka", "artist": "Maman Fvndy", "thumbnail": "https://i.ytimg.com/vi/zTJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "42", "title": "Nan Ko Paham", "artist": "Maman Fvndy", "thumbnail": "https://i.ytimg.com/vi/ATJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "43", "title": "Cinta Dalam Duka", "artist": "Arief", "thumbnail": "https://i.ytimg.com/vi/BTJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "44", "title": "WEDI DOSA", "artist": "Missel Laura D", "thumbnail": "https://i.ytimg.com/vi/CTJ4x1wY4n0/hqdefault.jpg"},
                    ]
                },
                {
                    "id": "viral_tiktok",
                    "title": "Viral TikTok",
                    "type": "grid",
                    "items": [
                        {"id": "45", "title": "Rindu Aku Rindu Kamu", "artist": "Maman Fvndy", "thumbnail": "https://i.ytimg.com/vi/DTJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "46", "title": "SOUND JJ PRESET FYP TIKTOK", "artist": "ARUL PCM", "thumbnail": "https://i.ytimg.com/vi/ETJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "47", "title": "DJ PALING ENAK", "artist": "Kristiwa Napu", "thumbnail": "https://i.ytimg.com/vi/FTJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "48", "title": "Jedag Jedug Preman", "artist": "Afrian Af", "thumbnail": "https://i.ytimg.com/vi/GTJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "49", "title": "#jedagjedug", "artist": "Zachz Winner", "thumbnail": "https://i.ytimg.com/vi/HTJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "50", "title": "Tabola Bale", "artist": "Maman Fvndy", "thumbnail": "https://i.ytimg.com/vi/ITJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "51", "title": "DJ Raiso Ngapusi", "artist": "Adit Fvnky Rmx", "thumbnail": "https://i.ytimg.com/vi/JTJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "52", "title": "Tia Monika (Remix)", "artist": "Maman Fvndy", "thumbnail": "https://i.ytimg.com/vi/KTJ4x1wY4n0/hqdefault.jpg"},
                    ]
                },
                {
                    "id": "artis_populer",
                    "title": "Artis Terpopuler Saat Ini",
                    "type": "artist",
                    "items": [
                        {"id": "53", "title": "Hati Yang Luka", "type": "Artis", "thumbnail": "https://i.ytimg.com/vi/LTJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "54", "title": "Tentang Rasa", "type": "Artis", "thumbnail": "https://i.ytimg.com/vi/MTJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "55", "title": "Bila Cinta Di Dusta", "type": "Artis", "thumbnail": "https://i.ytimg.com/vi/NTJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "56", "title": "Mencari Alasan", "type": "Artis", "thumbnail": "https://i.ytimg.com/vi/OTJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "57", "title": "Bersama Bintang", "type": "Artis", "thumbnail": "https://i.ytimg.com/vi/PTJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "58", "title": "Hanya Rindu", "type": "Artis", "thumbnail": "https://i.ytimg.com/vi/QTJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "59", "title": "Satu Nama Tetap Di Hati", "type": "Artis", "thumbnail": "https://i.ytimg.com/vi/RTJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "60", "title": "Keras Kepala", "type": "Artis", "thumbnail": "https://i.ytimg.com/vi/STJ4x1wY4n0/hqdefault.jpg"},
                    ]
                },
                {
                    "id": "hit_hari_ini",
                    "title": "Hit terpopuler hari ini",
                    "type": "grid",
                    "items": [
                        {"id": "61", "title": "Anugerah Terindah", "artist": "Andmesh", "thumbnail": "https://i.ytimg.com/vi/TTJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "62", "title": "Rahasia Hati", "artist": "NIDJI", "thumbnail": "https://i.ytimg.com/vi/UTJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "63", "title": "Kehadiranmu", "artist": "Vagetoz", "thumbnail": "https://i.ytimg.com/vi/VTJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "64", "title": "Tujh Mein Rab Dikhta Hai", "artist": "Roop Kumar Rathod", "thumbnail": "https://i.ytimg.com/vi/WTJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "65", "title": "Nanti Kita Seperti Ini", "artist": "BATAS SENJA", "thumbnail": "https://i.ytimg.com/vi/XTJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "66", "title": "Satu Rasa Cinta (feat. Difarina Indra Adella)", "artist": "Fendik Adella", "thumbnail": "https://i.ytimg.com/vi/YTJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "67", "title": "Sinarengan (feat. Bella Bonita)", "artist": "Denny Caknan", "thumbnail": "https://i.ytimg.com/vi/ZTJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "68", "title": "Bunga Abadi", "artist": "Rio Clappy", "thumbnail": "https://i.ytimg.com/vi/aUJ4x1wY4n0/hqdefault.jpg"},
                    ]
                },
                {
                    "id": "tiktok_playlist",
                    "title": "Dibuat Untuk TikTok",
                    "type": "grid",
                    "items": [
                        {"id": "69", "title": "Playlist For TikTok Content", "artist": "DJ TikTok", "thumbnail": "https://i.ytimg.com/vi/bUJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "70", "title": "Garam Dan Madu", "artist": "Maman Fvndy", "thumbnail": "https://i.ytimg.com/vi/cUJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "71", "title": "Infinity", "artist": "Jaymes Young", "thumbnail": "https://i.ytimg.com/vi/dUJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "72", "title": "Playlist For TikTok", "artist": "TikTok Music", "thumbnail": "https://i.ytimg.com/vi/eUJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "73", "title": "Playlist For TikTok", "artist": "TikTok Music", "thumbnail": "https://i.ytimg.com/vi/fUJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "74", "title": "TikTok Playlist", "artist": "TikTokHub", "thumbnail": "https://i.ytimg.com/vi/gUJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "75", "title": "Playlist For TikTok", "artist": "TikTok Music", "thumbnail": "https://i.ytimg.com/vi/hUJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "76", "title": "TikTok Trap Beats Playlist", "artist": "TikTokHub", "thumbnail": "https://i.ytimg.com/vi/iUJ4x1wY4n0/hqdefault.jpg"},
                    ]
                },
                {
                    "id": "album_populer",
                    "title": "Album dan single populer",
                    "type": "grid",
                    "items": [
                        {"id": "77", "title": "Baby (feat. Ludacris)", "artist": "Justin Bieber", "thumbnail": "https://i.ytimg.com/vi/kffacxfA7G4/hqdefault.jpg"},
                        {"id": "78", "title": "Hotel California", "artist": "Eagles", "thumbnail": "https://i.ytimg.com/vi/BciS5krYL80/hqdefault.jpg"},
                        {"id": "79", "title": "ANDAI TAK BERPISAH", "artist": "Rheina official", "thumbnail": "https://i.ytimg.com/vi/lUJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "80", "title": "Levitating", "artist": "Dua Lipa", "thumbnail": "https://i.ytimg.com/vi/TUVcZfQe-Kw/hqdefault.jpg"},
                        {"id": "81", "title": "One Time", "artist": "Justin Bieber", "thumbnail": "https://i.ytimg.com/vi/CHVhwcOg6y8/hqdefault.jpg"},
                        {"id": "82", "title": "I Wanna Dance with Somebody (Who Loves Me)", "artist": "Whitney Houston", "thumbnail": "https://i.ytimg.com/vi/eH3giaIzONA/hqdefault.jpg"},
                        {"id": "83", "title": "Shape of You", "artist": "Ed Sheeran", "thumbnail": "https://i.ytimg.com/vi/JGwWNGJdvx8/hqdefault.jpg"},
                        {"id": "84", "title": "You'll Be in My Heart", "artist": "NIKI", "thumbnail": "https://i.ytimg.com/vi/mUJ4x1wY4n0/hqdefault.jpg"},
                    ]
                }
            ]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ============== SEARCH ENDPOINTS ==============

@app.get("/api/search")
async def search(query: str = Query(..., min_length=1)):
    """Search for songs, artists, albums"""
    try:
        results = ytmusic.search(query, filter="songs", limit=20)
        return {"results": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/categories")
async def get_categories():
    """Get browse categories"""
    return {
        "categories": [
            {"id": "made-for-you", "name": "Dibuat Untuk Kamu", "color": "#8B5CF6"},
            {"id": "upcoming", "name": "Rilis Mendatang", "color": "#10B981"},
            {"id": "new-releases", "name": "Rilis Baru", "color": "#84CC16"},
            {"id": "ramadan", "name": "Ramadan", "color": "#10B981"},
            {"id": "pop", "name": "Pop", "color": "#3B82F6"},
            {"id": "indie", "name": "Indie", "color": "#EC4899"},
            {"id": "indonesian", "name": "Musik Indonesia", "color": "#EF4444"},
            {"id": "charts", "name": "Tangga Lagu", "color": "#8B5CF6"},
            {"id": "podcast", "name": "Peringkat Podcast", "color": "#1E3A8A"},
            {"id": "kpop", "name": "K-pop", "color": "#EC4899"},
        ]
    }

# ============== MUSIC ENDPOINTS ==============

@app.get("/api/song/{video_id}")
async def get_song_info(video_id: str):
    """Get song information"""
    try:
        song_info = ytmusic.get_song(video_id)
        return song_info
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/stream/{video_id}")
async def get_stream_url(video_id: str):
    """Get stream URL for a song"""
    try:
        song_info = ytmusic.get_song(video_id)
        # Return the streaming URL
        return {"stream_url": f"https://music.youtube.com/watch?v={video_id}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ============== ARTIST ENDPOINTS ==============

@app.get("/api/artist/{channel_id}")
async def get_artist_info(channel_id: str):
    """Get artist information"""
    try:
        artist_info = ytmusic.get_artist(channel_id)
        return artist_info
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ============== PLAYLIST ENDPOINTS ==============

@app.get("/api/playlist/{playlist_id}")
async def get_playlist(playlist_id: str):
    """Get playlist information"""
    try:
        playlist_info = ytmusic.get_playlist(playlist_id)
        return playlist_info
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ============== CHARTS ENDPOINTS ==============

@app.get("/api/charts")
async def get_charts(country: str = "ID"):
    """Get music charts for a country"""
    try:
        charts = ytmusic.get_charts(country=country)
        return charts
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ============== STATIC FILES ==============

# Mount static files
frontend_path = os.path.join(os.path.dirname(__file__), "..", "frontend")
if os.path.exists(frontend_path):
    app.mount("/", StaticFiles(directory=frontend_path, html=True), name="frontend")

@app.get("/")
async def root():
    return FileResponse(os.path.join(frontend_path, "index.html"))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
