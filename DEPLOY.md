# Deploy Web Music ke Vercel

## Cara Deploy Full-Stack (Frontend + Backend)

### 1. Install Vercel CLI
```bash
npm i -g vercel
```

### 2. Login ke Vercel
```bash
vercel login
```

### 3. Deploy Project
```bash
cd /path/to/music-player
vercel --prod
```

## Struktur Project untuk Vercel

```
music-player/
├── api/
│   ├── index.py              # FastAPI backend (Vercel Serverless Function)
│   └── requirements.txt      # Python dependencies
├── public/                   # Static frontend files
│   ├── index.html
│   ├── css/
│   ├── js/
│   ├── assets/
│   ├── manifest.json
│   └── sw.js
├── vercel.json               # Vercel configuration
└── README.md
```

## API Endpoints (Setelah Deploy)

| Endpoint | Deskripsi |
|----------|-----------|
| `https://your-app.vercel.app/api/home` | Get home content |
| `https://your-app.vercel.app/api/search?query=lagu` | Search musik |
| `https://your-app.vercel.app/api/categories` | Get kategori |
| `https://your-app.vercel.app/api/song/{video_id}` | Get song info |
| `https://your-app.vercel.app/api/stream/{video_id}` | Get stream URL |

## Fitur yang Berfungsi Setelah Deploy

✅ **Search Musik** - Bisa cari lagu dari YouTube Music database
✅ **Play Lagu** - Stream lagu dari YouTube Music (via ytmusicapi)
✅ **Home Content** - Load section musik dari API
✅ **Categories** - Kategori musik berwarna-warni
✅ **IndexedDB** - Penyimpanan lokal untuk liked songs & recently played
✅ **PWA** - Bisa diinstall sebagai aplikasi

## Catatan Penting

1. **ytmusicapi** di Vercel: Library ini akan bekerja di Vercel Serverless Functions
2. **CORS**: Sudah di-enable untuk semua origin
3. **Rate Limit**: YouTube Music API mungkin memiliki rate limit
4. **Stream URL**: Stream URL dari YouTube Music bersifat temporary dan perlu di-refresh

## Troubleshooting

### Jika API Error
- Check Vercel Logs: `vercel logs --tail`
- Pastikan `requirements.txt` sudah benar
- Pastikan `vercel.json` routing sudah benar

### Jika Frontend Tidak Load
- Pastikan folder `public/` ada di root project
- Check browser console untuk error
- Pastikan API_BASE_URL di `app.js` sudah benar
