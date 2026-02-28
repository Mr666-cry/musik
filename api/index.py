from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from ytmusicapi import YTMusic
from mangum import Mangum

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
        return {
            "sections": [
                {
                    "id": "sering_dengarkan",
                    "title": "Sering kamu dengarkan",
                    "type": "horizontal",
                    "items": [
                        {"id": "6nJ1C1kN3sE", "title": "Satu Rasa Cinta", "artist": "Arief", "thumbnail": "https://i.ytimg.com/vi/6nJ1C1kN3sE/hqdefault.jpg"},
                        {"id": "7Jz9vG8k5sQ", "title": "TABOLA BALE", "artist": "SILET OPEN UP", "thumbnail": "https://i.ytimg.com/vi/7Jz9vG8k5sQ/hqdefault.jpg"},
                        {"id": "8Kz9vG8k5sQ", "title": "KUMPULAN LAGU POP KARO", "artist": "Narta Siregar", "thumbnail": "https://i.ytimg.com/vi/8Kz9vG8k5sQ/hqdefault.jpg"},
                        {"id": "9Lz9vG8k5sQ", "title": "Bahagia Lagi", "artist": "Piche Kota", "thumbnail": "https://i.ytimg.com/vi/9Lz9vG8k5sQ/hqdefault.jpg"},
                    ]
                },
                {
                    "id": "rilis_anyar",
                    "title": "Rilis Anyar (Baru Rilis)",
                    "type": "grid",
                    "items": [
                        {"id": "MPJ4x1wY4n0", "title": "Tanpa Cinta", "artist": "Yovie Widianto", "thumbnail": "https://i.ytimg.com/vi/MPJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "QQJ4x1wY4n0", "title": "Merayu Tuhan", "artist": "Tri Suaka", "thumbnail": "https://i.ytimg.com/vi/QQJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "RRJ4x1wY4n0", "title": "Kita Usahakan Lagi", "artist": "Batas Senja", "thumbnail": "https://i.ytimg.com/vi/RRJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "SRJ4x1wY4n0", "title": "LET ME DEFEAT", "artist": "Teras Entertaiment", "thumbnail": "https://i.ytimg.com/vi/SRJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "TRJ4x1wY4n0", "title": "Tunggal Eka", "artist": "Denny Caknan", "thumbnail": "https://i.ytimg.com/vi/TRJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "URJ4x1wY4n0", "title": "Dan...", "artist": "Sheila On 7", "thumbnail": "https://i.ytimg.com/vi/URJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "VRJ4x1wY4n0", "title": "Goodbye Lover", "artist": "Teras Entertaiment", "thumbnail": "https://i.ytimg.com/vi/VRJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "WRJ4x1wY4n0", "title": "Tunggu Saja", "artist": "Radja", "thumbnail": "https://i.ytimg.com/vi/WRJ4x1wY4n0/hqdefault.jpg"},
                    ]
                },
                {
                    "id": "gembira_semangat",
                    "title": "Gembira & Semangat",
                    "type": "grid",
                    "items": [
                        {"id": "XSJ4x1wY4n0", "title": "Tetap Semangat", "artist": "Bondan Prakoso", "thumbnail": "https://i.ytimg.com/vi/XSJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "YSJ4x1wY4n0", "title": "Ayo Semangat", "artist": "Nada Swara Gembira", "thumbnail": "https://i.ytimg.com/vi/YSJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "ZSJ4x1wY4n0", "title": "Hati Gembira", "artist": "Tentang Anak", "thumbnail": "https://i.ytimg.com/vi/ZSJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "aTJ4x1wY4n0", "title": "Gembira Adalah Obat", "artist": "Tony Q Rastafara", "thumbnail": "https://i.ytimg.com/vi/aTJ4x1wY4n0/hqdefault.jpg"},
                    ]
                },
                {
                    "id": "tangga_lagu",
                    "title": "Tangga Lagu Populer",
                    "type": "grid",
                    "items": [
                        {"id": "fTJ4x1wY4n0", "title": "Zen Meditation Music", "artist": "Nature Sounds", "thumbnail": "https://i.ytimg.com/vi/fTJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "gTJ4x1wY4n0", "title": "Hours Relaxing Guitar", "artist": "Nature Sounds", "thumbnail": "https://i.ytimg.com/vi/gTJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "hTJ4x1wY4n0", "title": "Coffee Shop Music", "artist": "Relaxing Piano Life", "thumbnail": "https://i.ytimg.com/vi/hTJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "iTJ4x1wY4n0", "title": "BEST GUITAR ROMANTIC", "artist": "Acoustic Guitar Music", "thumbnail": "https://i.ytimg.com/vi/iTJ4x1wY4n0/hqdefault.jpg"},
                    ]
                },
                {
                    "id": "galau_terpopuler",
                    "title": "Galau Terpopuler",
                    "type": "grid",
                    "items": [
                        {"id": "nTJ4x1wY4n0", "title": "Bertahan Sakit Pergi Sulit", "artist": "Syahriyadi", "thumbnail": "https://i.ytimg.com/vi/nTJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "oTJ4x1wY4n0", "title": "Lumpuhkan Ingatanku", "artist": "Geisha", "thumbnail": "https://i.ytimg.com/vi/oTJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "pTJ4x1wY4n0", "title": "Kenangan Terindah", "artist": "SAMSONS", "thumbnail": "https://i.ytimg.com/vi/pTJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "qTJ4x1wY4n0", "title": "Jiwa Yang Bersedih", "artist": "Ghea Indrawari", "thumbnail": "https://i.ytimg.com/vi/qTJ4x1wY4n0/hqdefault.jpg"},
                    ]
                },
                {
                    "id": "baru_diputar",
                    "title": "Baru diputar",
                    "type": "grid",
                    "items": [
                        {"id": "vTJ4x1wY4n0", "title": "Cinta Merah Jambu", "artist": "LEK PANG", "thumbnail": "https://i.ytimg.com/vi/vTJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "wTJ4x1wY4n0", "title": "Aku Dah Lupa", "artist": "Maman Fvndy", "thumbnail": "https://i.ytimg.com/vi/wTJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "xTJ4x1wY4n0", "title": "Asmara Kerinduan", "artist": "Meyda Rahma", "thumbnail": "https://i.ytimg.com/vi/xTJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "yTJ4x1wY4n0", "title": "KUAN SOE LEKONES", "artist": "AITINA MUSIK", "thumbnail": "https://i.ytimg.com/vi/yTJ4x1wY4n0/hqdefault.jpg"},
                    ]
                },
                {
                    "id": "viral_tiktok",
                    "title": "Viral TikTok",
                    "type": "grid",
                    "items": [
                        {"id": "DTJ4x1wY4n0", "title": "Rindu Aku Rindu Kamu", "artist": "Maman Fvndy", "thumbnail": "https://i.ytimg.com/vi/DTJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "ETJ4x1wY4n0", "title": "SOUND JJ PRESET", "artist": "ARUL PCM", "thumbnail": "https://i.ytimg.com/vi/ETJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "FTJ4x1wY4n0", "title": "DJ PALING ENAK", "artist": "Kristiwa Napu", "thumbnail": "https://i.ytimg.com/vi/FTJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "GTJ4x1wY4n0", "title": "Jedag Jedug Preman", "artist": "Afrian Af", "thumbnail": "https://i.ytimg.com/vi/GTJ4x1wY4n0/hqdefault.jpg"},
                    ]
                },
                {
                    "id": "artis_populer",
                    "title": "Artis Terpopuler Saat Ini",
                    "type": "artist",
                    "items": [
                        {"id": "LTJ4x1wY4n0", "title": "Hati Yang Luka", "type": "Artis", "thumbnail": "https://i.ytimg.com/vi/LTJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "MTJ4x1wY4n0", "title": "Tentang Rasa", "type": "Artis", "thumbnail": "https://i.ytimg.com/vi/MTJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "NTJ4x1wY4n0", "title": "Bila Cinta Di Dusta", "type": "Artis", "thumbnail": "https://i.ytimg.com/vi/NTJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "OTJ4x1wY4n0", "title": "Mencari Alasan", "type": "Artis", "thumbnail": "https://i.ytimg.com/vi/OTJ4x1wY4n0/hqdefault.jpg"},
                    ]
                },
                {
                    "id": "hit_hari_ini",
                    "title": "Hit terpopuler hari ini",
                    "type": "grid",
                    "items": [
                        {"id": "TTJ4x1wY4n0", "title": "Anugerah Terindah", "artist": "Andmesh", "thumbnail": "https://i.ytimg.com/vi/TTJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "UTJ4x1wY4n0", "title": "Rahasia Hati", "artist": "NIDJI", "thumbnail": "https://i.ytimg.com/vi/UTJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "VTJ4x1wY4n0", "title": "Kehadiranmu", "artist": "Vagetoz", "thumbnail": "https://i.ytimg.com/vi/VTJ4x1wY4n0/hqdefault.jpg"},
                        {"id": "WTJ4x1wY4n0", "title": "Tujh Mein Rab Dikhta Hai", "artist": "Roop Kumar Rathod", "thumbnail": "https://i.ytimg.com/vi/WTJ4x1wY4n0/hqdefault.jpg"},
                    ]
                },
                {
                    "id": "album_populer",
                    "title": "Album dan single populer",
                    "type": "grid",
                    "items": [
                        {"id": "kffacxfA7G4", "title": "Baby (feat. Ludacris)", "artist": "Justin Bieber", "thumbnail": "https://i.ytimg.com/vi/kffacxfA7G4/hqdefault.jpg"},
                        {"id": "BciS5krYL80", "title": "Hotel California", "artist": "Eagles", "thumbnail": "https://i.ytimg.com/vi/BciS5krYL80/hqdefault.jpg"},
                        {"id": "TUVcZfQe-Kw", "title": "Levitating", "artist": "Dua Lipa", "thumbnail": "https://i.ytimg.com/vi/TUVcZfQe-Kw/hqdefault.jpg"},
                        {"id": "JGwWNGJdvx8", "title": "Shape of You", "artist": "Ed Sheeran", "thumbnail": "https://i.ytimg.com/vi/JGwWNGJdvx8/hqdefault.jpg"},
                    ]
                }
            ]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ============== SEARCH ENDPOINTS ==============

@app.get("/api/search")
async def search(query: str = Query(..., min_length=1)):
    """Search for songs, artists, albums using ytmusicapi"""
    try:
        results = ytmusic.search(query, filter="songs", limit=20)
        
        # Format results
        formatted_results = []
        for item in results:
            if item.get("resultType") == "song":
                formatted_results.append({
                    "id": item.get("videoId"),
                    "title": item.get("title"),
                    "artist": item.get("artists", [{}])[0].get("name", "Unknown") if item.get("artists") else "Unknown",
                    "thumbnail": item.get("thumbnails", [{}])[-1].get("url", "") if item.get("thumbnails") else "",
                    "duration": item.get("duration"),
                    "album": item.get("album", {}).get("name") if item.get("album") else None
                })
        
        return {"results": formatted_results}
    except Exception as e:
        # Fallback to mock data if API fails
        return {"results": get_mock_search_results(query)}

def get_mock_search_results(query):
    """Fallback mock search results"""
    all_songs = [
        {"id": "kffacxfA7G4", "title": "Baby", "artist": "Justin Bieber ft. Ludacris", "thumbnail": "https://i.ytimg.com/vi/kffacxfA7G4/hqdefault.jpg"},
        {"id": "JGwWNGJdvx8", "title": "Shape of You", "artist": "Ed Sheeran", "thumbnail": "https://i.ytimg.com/vi/JGwWNGJdvx8/hqdefault.jpg"},
        {"id": "TUVcZfQe-Kw", "title": "Levitating", "artist": "Dua Lipa", "thumbnail": "https://i.ytimg.com/vi/TUVcZfQe-Kw/hqdefault.jpg"},
        {"id": "BciS5krYL80", "title": "Hotel California", "artist": "Eagles", "thumbnail": "https://i.ytimg.com/vi/BciS5krYL80/hqdefault.jpg"},
        {"id": "eH3giaIzONA", "title": "I Wanna Dance With Somebody", "artist": "Whitney Houston", "thumbnail": "https://i.ytimg.com/vi/eH3giaIzONA/hqdefault.jpg"},
        {"id": "6nJ1C1kN3sE", "title": "Satu Rasa Cinta", "artist": "Arief", "thumbnail": "https://i.ytimg.com/vi/6nJ1C1kN3sE/hqdefault.jpg"},
        {"id": "MPJ4x1wY4n0", "title": "Tanpa Cinta", "artist": "Yovie Widianto", "thumbnail": "https://i.ytimg.com/vi/MPJ4x1wY4n0/hqdefault.jpg"},
        {"id": "TRJ4x1wY4n0", "title": "Tunggal Eka", "artist": "Denny Caknan", "thumbnail": "https://i.ytimg.com/vi/TRJ4x1wY4n0/hqdefault.jpg"},
    ]
    
    query_lower = query.lower()
    return [song for song in all_songs if query_lower in song["title"].lower() or query_lower in song["artist"].lower()]

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
    """Get song information from YouTube Music"""
    try:
        song_info = ytmusic.get_song(video_id)
        return song_info
    except Exception as e:
        # Return mock data if API fails
        return {
            "videoId": video_id,
            "title": "Unknown Song",
            "artist": "Unknown Artist",
            "thumbnail": f"https://i.ytimg.com/vi/{video_id}/hqdefault.jpg"
        }

@app.get("/api/stream/{video_id}")
async def get_stream_url(video_id: str):
    """Get stream URL for a song"""
    try:
        # Get streaming info from ytmusicapi
        song_info = ytmusic.get_song(video_id)
        
        # Return YouTube Music URL
        return {
            "stream_url": f"https://music.youtube.com/watch?v={video_id}",
            "video_id": video_id,
            "formats": [
                {"url": f"https://music.youtube.com/watch?v={video_id}", "quality": "high"}
            ]
        }
    except Exception as e:
        return {
            "stream_url": f"https://music.youtube.com/watch?v={video_id}",
            "video_id": video_id
        }

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
        # Return mock charts data
        return {
            "songs": [
                {"id": "kffacxfA7G4", "title": "Baby", "artist": "Justin Bieber"},
                {"id": "JGwWNGJdvx8", "title": "Shape of You", "artist": "Ed Sheeran"},
                {"id": "TUVcZfQe-Kw", "title": "Levitating", "artist": "Dua Lipa"},
            ]
        }

# ============== HEALTH CHECK ==============

@app.get("/api/health")
async def health_check():
    return {"status": "ok", "version": "2.3.0"}

# Vercel handler
handler = Mangum(app, lifespan="off")
