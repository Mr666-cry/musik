# SANN404 FORUM - Web Music

Aplikasi web musik dengan database global dan navigasi native-like, dibangun dengan FastAPI dan ytmusicapi.

## Fitur

- **Home Page**: Berbagai section musik (Sering kamu dengarkan, Rilis Anyar, Gembira & Semangat, Tangga Lagu Populer, dll)
- **Search**: Pencarian lagu dengan kategori yang berwarna-warni
- **Koleksi Kamu**: Playlist pribadi dan lagu yang disukai
- **Developer**: Informasi teknis tentang aplikasi
- **Music Player**: Player dengan kontrol play/pause, next/previous, dan progress bar
- **PWA**: Dapat diinstall sebagai aplikasi native
- **IndexedDB**: Penyimpanan lokal untuk lagu yang disukai dan recently played

## Teknologi

### Frontend Core
- HTML5 / CSS3 / JavaScript
- Progressive Web App (PWA)
- Service Worker
- IndexedDB API

### Backend API
- FastAPI (Python)
- ytmusicapi (YouTube Music API)
- CORS enabled

## Struktur Project

```
music-player/
├── backend/
│   ├── main.py              # FastAPI main application
│   └── requirements.txt     # Python dependencies
├── frontend/
│   ├── index.html           # Main HTML file
│   ├── css/
│   │   └── style.css        # Stylesheet
│   ├── js/
│   │   ├── db.js            # IndexedDB manager
│   │   └── app.js           # Main application logic
│   ├── assets/              # Icons and images
│   ├── manifest.json        # PWA manifest
│   └── sw.js                # Service Worker
└── README.md
```

## Cara Menjalankan

### 1. Install Dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 2. Jalankan Backend

```bash
python main.py
```

Backend akan berjalan di `http://localhost:8000`

### 3. Jalankan Frontend

Untuk development, gunakan live server atau buka `frontend/index.html` langsung.

Untuk production dengan backend:
```bash
# Backend sudah serve static files dari frontend folder
# Buka http://localhost:8000
```

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/home` | GET | Get home page content |
| `/api/search?query={q}` | GET | Search songs |
| `/api/categories` | GET | Get browse categories |
| `/api/song/{video_id}` | GET | Get song info |
| `/api/stream/{video_id}` | GET | Get stream URL |
| `/api/artist/{channel_id}` | GET | Get artist info |
| `/api/playlist/{playlist_id}` | GET | Get playlist info |
| `/api/charts` | GET | Get music charts |

## IndexedDB Stores

- `likedSongs`: Lagu yang disukai user
- `recentlyPlayed`: Riwayat pemutaran
- `playlists`: Playlist user
- `queue`: Antrian pemutaran
- `preferences`: Preferensi user

## PWA Features

- Installable sebagai aplikasi native
- Offline support dengan caching
- Background sync
- Push notifications (opsional)

## Versi

v2.3.0 - Sistem Online

## Developer

SANN404 FORUM - Lead Developer & UI/UX Designer

## License

Hak Cipta © 2026 SANN404 FORUM
