// ===== IndexedDB Database Manager =====
const DB_NAME = 'WebMusicDB';
const DB_VERSION = 1;

class MusicDatabase {
    constructor() {
        this.db = null;
        this.init();
    }

    async init() {
        return new Promise((resolve, reject) => {
            const request = indexedDB.open(DB_NAME, DB_VERSION);

            request.onerror = () => {
                console.error('Error opening database:', request.error);
                reject(request.error);
            };

            request.onsuccess = () => {
                this.db = request.result;
                console.log('Database opened successfully');
                resolve(this.db);
            };

            request.onupgradeneeded = (event) => {
                const db = event.target.result;

                // Store for liked songs
                if (!db.objectStoreNames.contains('likedSongs')) {
                    const likedStore = db.createObjectStore('likedSongs', { keyPath: 'id' });
                    likedStore.createIndex('title', 'title', { unique: false });
                    likedStore.createIndex('artist', 'artist', { unique: false });
                    likedStore.createIndex('addedAt', 'addedAt', { unique: false });
                }

                // Store for playlists
                if (!db.objectStoreNames.contains('playlists')) {
                    const playlistStore = db.createObjectStore('playlists', { keyPath: 'id' });
                    playlistStore.createIndex('name', 'name', { unique: false });
                    playlistStore.createIndex('createdAt', 'createdAt', { unique: false });
                }

                // Store for recently played
                if (!db.objectStoreNames.contains('recentlyPlayed')) {
                    const recentStore = db.createObjectStore('recentlyPlayed', { keyPath: 'id' });
                    recentStore.createIndex('playedAt', 'playedAt', { unique: false });
                }

                // Store for queue
                if (!db.objectStoreNames.contains('queue')) {
                    const queueStore = db.createObjectStore('queue', { keyPath: 'id' });
                    queueStore.createIndex('position', 'position', { unique: false });
                }

                // Store for user preferences
                if (!db.objectStoreNames.contains('preferences')) {
                    db.createObjectStore('preferences', { keyPath: 'key' });
                }
            };
        });
    }

    // ===== Liked Songs Methods =====
    async addLikedSong(song) {
        return new Promise((resolve, reject) => {
            const transaction = this.db.transaction(['likedSongs'], 'readwrite');
            const store = transaction.objectStore('likedSongs');
            
            const songData = {
                ...song,
                addedAt: new Date().toISOString()
            };

            const request = store.put(songData);

            request.onsuccess = () => resolve(songData);
            request.onerror = () => reject(request.error);
        });
    }

    async removeLikedSong(songId) {
        return new Promise((resolve, reject) => {
            const transaction = this.db.transaction(['likedSongs'], 'readwrite');
            const store = transaction.objectStore('likedSongs');
            const request = store.delete(songId);

            request.onsuccess = () => resolve(true);
            request.onerror = () => reject(request.error);
        });
    }

    async getLikedSongs() {
        return new Promise((resolve, reject) => {
            const transaction = this.db.transaction(['likedSongs'], 'readonly');
            const store = transaction.objectStore('likedSongs');
            const request = store.getAll();

            request.onsuccess = () => resolve(request.result);
            request.onerror = () => reject(request.error);
        });
    }

    async isLiked(songId) {
        return new Promise((resolve, reject) => {
            const transaction = this.db.transaction(['likedSongs'], 'readonly');
            const store = transaction.objectStore('likedSongs');
            const request = store.get(songId);

            request.onsuccess = () => resolve(!!request.result);
            request.onerror = () => reject(request.error);
        });
    }

    // ===== Recently Played Methods =====
    async addToRecentlyPlayed(song) {
        return new Promise((resolve, reject) => {
            const transaction = this.db.transaction(['recentlyPlayed'], 'readwrite');
            const store = transaction.objectStore('recentlyPlayed');
            
            const songData = {
                ...song,
                playedAt: new Date().toISOString()
            };

            const request = store.put(songData);

            request.onsuccess = () => {
                // Keep only last 50 songs
                this.trimRecentlyPlayed(50);
                resolve(songData);
            };
            request.onerror = () => reject(request.error);
        });
    }

    async trimRecentlyPlayed(maxCount) {
        const songs = await this.getRecentlyPlayed();
        if (songs.length > maxCount) {
            const toDelete = songs.slice(maxCount);
            for (const song of toDelete) {
                await this.deleteFromRecentlyPlayed(song.id);
            }
        }
    }

    async deleteFromRecentlyPlayed(songId) {
        return new Promise((resolve, reject) => {
            const transaction = this.db.transaction(['recentlyPlayed'], 'readwrite');
            const store = transaction.objectStore('recentlyPlayed');
            const request = store.delete(songId);

            request.onsuccess = () => resolve(true);
            request.onerror = () => reject(request.error);
        });
    }

    async getRecentlyPlayed(limit = 20) {
        return new Promise((resolve, reject) => {
            const transaction = this.db.transaction(['recentlyPlayed'], 'readonly');
            const store = transaction.objectStore('recentlyPlayed');
            const index = store.index('playedAt');
            const request = index.openCursor(null, 'prev');

            const results = [];
            request.onsuccess = (event) => {
                const cursor = event.target.result;
                if (cursor && results.length < limit) {
                    results.push(cursor.value);
                    cursor.continue();
                } else {
                    resolve(results);
                }
            };
            request.onerror = () => reject(request.error);
        });
    }

    // ===== Queue Methods =====
    async addToQueue(song, position = null) {
        return new Promise((resolve, reject) => {
            const transaction = this.db.transaction(['queue'], 'readwrite');
            const store = transaction.objectStore('queue');
            
            const songData = {
                ...song,
                position: position || Date.now()
            };

            const request = store.put(songData);

            request.onsuccess = () => resolve(songData);
            request.onerror = () => reject(request.error);
        });
    }

    async removeFromQueue(songId) {
        return new Promise((resolve, reject) => {
            const transaction = this.db.transaction(['queue'], 'readwrite');
            const store = transaction.objectStore('queue');
            const request = store.delete(songId);

            request.onsuccess = () => resolve(true);
            request.onerror = () => reject(request.error);
        });
    }

    async getQueue() {
        return new Promise((resolve, reject) => {
            const transaction = this.db.transaction(['queue'], 'readonly');
            const store = transaction.objectStore('queue');
            const index = store.index('position');
            const request = index.getAll();

            request.onsuccess = () => resolve(request.result);
            request.onerror = () => reject(request.error);
        });
    }

    async clearQueue() {
        return new Promise((resolve, reject) => {
            const transaction = this.db.transaction(['queue'], 'readwrite');
            const store = transaction.objectStore('queue');
            const request = store.clear();

            request.onsuccess = () => resolve(true);
            request.onerror = () => reject(request.error);
        });
    }

    // ===== Playlist Methods =====
    async createPlaylist(name, description = '') {
        return new Promise((resolve, reject) => {
            const transaction = this.db.transaction(['playlists'], 'readwrite');
            const store = transaction.objectStore('playlists');
            
            const playlist = {
                id: 'playlist_' + Date.now(),
                name,
                description,
                songs: [],
                createdAt: new Date().toISOString(),
                updatedAt: new Date().toISOString()
            };

            const request = store.put(playlist);

            request.onsuccess = () => resolve(playlist);
            request.onerror = () => reject(request.error);
        });
    }

    async addSongToPlaylist(playlistId, song) {
        return new Promise((resolve, reject) => {
            const transaction = this.db.transaction(['playlists'], 'readwrite');
            const store = transaction.objectStore('playlists');
            const request = store.get(playlistId);

            request.onsuccess = () => {
                const playlist = request.result;
                if (playlist) {
                    playlist.songs.push(song);
                    playlist.updatedAt = new Date().toISOString();
                    const updateRequest = store.put(playlist);
                    updateRequest.onsuccess = () => resolve(playlist);
                    updateRequest.onerror = () => reject(updateRequest.error);
                } else {
                    reject(new Error('Playlist not found'));
                }
            };
            request.onerror = () => reject(request.error);
        });
    }

    async getPlaylists() {
        return new Promise((resolve, reject) => {
            const transaction = this.db.transaction(['playlists'], 'readonly');
            const store = transaction.objectStore('playlists');
            const request = store.getAll();

            request.onsuccess = () => resolve(request.result);
            request.onerror = () => reject(request.error);
        });
    }

    // ===== Preferences Methods =====
    async setPreference(key, value) {
        return new Promise((resolve, reject) => {
            const transaction = this.db.transaction(['preferences'], 'readwrite');
            const store = transaction.objectStore('preferences');
            const request = store.put({ key, value });

            request.onsuccess = () => resolve(true);
            request.onerror = () => reject(request.error);
        });
    }

    async getPreference(key, defaultValue = null) {
        return new Promise((resolve, reject) => {
            const transaction = this.db.transaction(['preferences'], 'readonly');
            const store = transaction.objectStore('preferences');
            const request = store.get(key);

            request.onsuccess = () => {
                resolve(request.result ? request.result.value : defaultValue);
            };
            request.onerror = () => reject(request.error);
        });
    }

    // ===== Statistics =====
    async getStats() {
        const [likedSongs, recentlyPlayed, playlists] = await Promise.all([
            this.getLikedSongs(),
            this.getRecentlyPlayed(),
            this.getPlaylists()
        ]);

        return {
            likedSongsCount: likedSongs.length,
            recentlyPlayedCount: recentlyPlayed.length,
            playlistsCount: playlists.length
        };
    }
}

// Create global instance
const musicDB = new MusicDatabase();
