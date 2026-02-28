// ===== Web Music Player Application =====
const API_BASE_URL = window.location.hostname === 'localhost' ? 'http://localhost:8000/api' : '/api';

// ===== App State =====
const state = {
    currentPage: 'home',
    currentSong: null,
    isPlaying: false,
    queue: [],
    currentIndex: 0,
    likedSongs: [],
    recentlyPlayed: [],
    homeData: null
};

// ===== DOM Elements =====
const elements = {
    pages: document.querySelectorAll('.page'),
    navItems: document.querySelectorAll('.nav-item'),
    tabBtns: document.querySelectorAll('.tab-btn'),
    playerBar: document.getElementById('player-bar'),
    fullPlayer: document.getElementById('full-player'),
    audioPlayer: document.getElementById('audio-player'),
    toast: document.getElementById('toast'),
    searchInput: document.getElementById('search-input'),
    searchResults: document.getElementById('search-results'),
    categoryGrid: document.getElementById('category-grid'),
    likedCount: document.getElementById('liked-count')
};

// ===== Initialization =====
document.addEventListener('DOMContentLoaded', async () => {
    await initApp();
});

async function initApp() {
    // Initialize database
    await musicDB.init();
    
    // Load saved data
    await loadLikedSongs();
    await loadRecentlyPlayed();
    
    // Setup event listeners
    setupNavigation();
    setupTabs();
    setupPlayer();
    setupSearch();
    
    // Load home content
    await loadHomeContent();
    
    // Load categories
    loadCategories();
    
    // Setup PWA
    setupPWA();
}

// ===== Navigation =====
function setupNavigation() {
    elements.navItems.forEach(item => {
        item.addEventListener('click', () => {
            const page = item.dataset.page;
            navigateTo(page);
        });
    });
}

function navigateTo(page) {
    state.currentPage = page;
    
    // Update nav items
    elements.navItems.forEach(item => {
        item.classList.toggle('active', item.dataset.page === page);
    });
    
    // Update pages
    elements.pages.forEach(p => {
        p.classList.toggle('active', p.id === `page-${page}`);
    });
    
    // Update header visibility
    const header = document.getElementById('header');
    if (page === 'developer' || page === 'collection') {
        header.style.display = 'none';
    } else {
        header.style.display = 'flex';
    }
    
    // Scroll to top
    const activePage = document.getElementById(`page-${page}`);
    if (activePage) {
        activePage.scrollTop = 0;
    }
}

// ===== Tabs =====
function setupTabs() {
    elements.tabBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            elements.tabBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            
            const tab = btn.dataset.tab;
            filterHomeContent(tab);
        });
    });
}

function filterHomeContent(tab) {
    const sections = document.querySelectorAll('.section');
    sections.forEach(section => {
        if (tab === 'semua') {
            section.style.display = 'block';
        } else if (tab === 'musik') {
            section.style.display = section.dataset.type !== 'podcast' ? 'block' : 'none';
        } else if (tab === 'podcast') {
            section.style.display = section.dataset.type === 'podcast' ? 'block' : 'none';
        }
    });
}

// ===== Home Content =====
async function loadHomeContent() {
    const contentScroll = document.querySelector('#page-home .content-scroll');
    
    try {
        // Fetch from API
        const response = await fetch(`${API_BASE_URL}/home`);
        const data = await response.json();
        state.homeData = data;
        
        renderHomeSections(contentScroll, data.sections);
    } catch (error) {
        console.error('Error loading home content:', error);
        // Fallback to mock data
        const data = getMockHomeData();
        state.homeData = data;
        renderHomeSections(contentScroll, data.sections);
    }
}

function getMockHomeData() {
    return {
        sections: [
            {
                id: 'sering_dengarkan',
                title: 'Sering kamu dengarkan',
                type: 'horizontal',
                items: [
                    { id: '1', title: 'Satu Rasa Cinta', artist: 'Arief', thumbnail: 'https://i.ytimg.com/vi/6nJ1C1kN3sE/hqdefault.jpg' },
                    { id: '2', title: 'TABOLA BALE', artist: 'SILET OPEN UP', thumbnail: 'https://i.ytimg.com/vi/7Jz9vG8k5sQ/hqdefault.jpg' },
                    { id: '3', title: 'KUMPULAN LAGU POP KARO', artist: 'Narta Siregar', thumbnail: 'https://i.ytimg.com/vi/8Kz9vG8k5sQ/hqdefault.jpg' },
                    { id: '4', title: 'Bahagia Lagi', artist: 'Piche Kota', thumbnail: 'https://i.ytimg.com/vi/9Lz9vG8k5sQ/hqdefault.jpg' },
                ]
            },
            {
                id: 'rilis_anyar',
                title: 'Rilis Anyar (Baru Rilis)',
                type: 'grid',
                items: [
                    { id: '5', title: 'Tanpa Cinta', artist: 'Yovie Widianto', thumbnail: 'https://i.ytimg.com/vi/MPJ4x1wY4n0/hqdefault.jpg' },
                    { id: '6', title: 'Merayu Tuhan', artist: 'Tri Suaka', thumbnail: 'https://i.ytimg.com/vi/QQJ4x1wY4n0/hqdefault.jpg' },
                    { id: '7', title: 'Kita Usahakan Lagi', artist: 'Batas Senja', thumbnail: 'https://i.ytimg.com/vi/RRJ4x1wY4n0/hqdefault.jpg' },
                    { id: '8', title: 'LET ME DEFEAT', artist: 'Teras Entertaiment', thumbnail: 'https://i.ytimg.com/vi/SRJ4x1wY4n0/hqdefault.jpg' },
                    { id: '9', title: 'Tunggal Eka', artist: 'Denny Caknan', thumbnail: 'https://i.ytimg.com/vi/TRJ4x1wY4n0/hqdefault.jpg' },
                    { id: '10', title: 'Dan...', artist: 'Sheila On 7', thumbnail: 'https://i.ytimg.com/vi/URJ4x1wY4n0/hqdefault.jpg' },
                    { id: '11', title: 'Goodbye Lover', artist: 'Teras Entertaiment', thumbnail: 'https://i.ytimg.com/vi/VRJ4x1wY4n0/hqdefault.jpg' },
                    { id: '12', title: 'Tunggu Saja', artist: 'Radja', thumbnail: 'https://i.ytimg.com/vi/WRJ4x1wY4n0/hqdefault.jpg' },
                ]
            },
            {
                id: 'gembira_semangat',
                title: 'Gembira & Semangat',
                type: 'grid',
                items: [
                    { id: '13', title: 'Tetap Semangat', artist: 'Bondan Prakoso', thumbnail: 'https://i.ytimg.com/vi/XSJ4x1wY4n0/hqdefault.jpg' },
                    { id: '14', title: 'Ayo Semangat', artist: 'Nada Swara Gembira', thumbnail: 'https://i.ytimg.com/vi/YSJ4x1wY4n0/hqdefault.jpg' },
                    { id: '15', title: 'Hati Gembira', artist: 'Tentang Anak', thumbnail: 'https://i.ytimg.com/vi/ZSJ4x1wY4n0/hqdefault.jpg' },
                    { id: '16', title: 'Gembira Adalah Obat', artist: 'Tony Q Rastafara', thumbnail: 'https://i.ytimg.com/vi/aTJ4x1wY4n0/hqdefault.jpg' },
                    { id: '17', title: 'Da Natiniptip Sanggar', artist: 'Maxima', thumbnail: 'https://i.ytimg.com/vi/bTJ4x1wY4n0/hqdefault.jpg' },
                    { id: '18', title: 'Semenjak Ada Dirimu', artist: 'Yovie Widianto', thumbnail: 'https://i.ytimg.com/vi/cTJ4x1wY4n0/hqdefault.jpg' },
                    { id: '19', title: 'Happy Music', artist: 'Nusantarian Dub', thumbnail: 'https://i.ytimg.com/vi/dTJ4x1wY4n0/hqdefault.jpg' },
                    { id: '20', title: 'Pagi Semangat!', artist: 'Lagu Anak Indonesia', thumbnail: 'https://i.ytimg.com/vi/eTJ4x1wY4n0/hqdefault.jpg' },
                ]
            },
            {
                id: 'tangga_lagu',
                title: 'Tangga Lagu Populer',
                type: 'grid',
                items: [
                    { id: '21', title: 'Zen Meditation Music', artist: 'Nature Sounds', thumbnail: 'https://i.ytimg.com/vi/fTJ4x1wY4n0/hqdefault.jpg' },
                    { id: '22', title: 'Hours Relaxing Guitar', artist: 'Nature Sounds', thumbnail: 'https://i.ytimg.com/vi/gTJ4x1wY4n0/hqdefault.jpg' },
                    { id: '23', title: 'Coffee Shop Music', artist: 'Relaxing Piano Life', thumbnail: 'https://i.ytimg.com/vi/hTJ4x1wY4n0/hqdefault.jpg' },
                    { id: '24', title: 'BEST GUITAR ROMANTIC', artist: 'Acoustic Guitar Music', thumbnail: 'https://i.ytimg.com/vi/iTJ4x1wY4n0/hqdefault.jpg' },
                    { id: '25', title: "Somebody's Pleasure", artist: 'Aziz Hedra', thumbnail: 'https://i.ytimg.com/vi/jTJ4x1wY4n0/hqdefault.jpg' },
                    { id: '26', title: 'Teenage Senorita Medley', artist: 'Victor Wood', thumbnail: 'https://i.ytimg.com/vi/kTJ4x1wY4n0/hqdefault.jpg' },
                    { id: '27', title: 'Dandelions', artist: 'Ruth B.', thumbnail: 'https://i.ytimg.com/vi/lTJ4x1wY4n0/hqdefault.jpg' },
                    { id: '28', title: 'R.I.O. Megamix', artist: 'R.I.O.', thumbnail: 'https://i.ytimg.com/vi/mTJ4x1wY4n0/hqdefault.jpg' },
                ]
            },
            {
                id: 'galau_terpopuler',
                title: 'Galau Terpopuler',
                type: 'grid',
                items: [
                    { id: '29', title: 'Bertahan Sakit Pergi Sulit', artist: 'Syahriyadi', thumbnail: 'https://i.ytimg.com/vi/nTJ4x1wY4n0/hqdefault.jpg' },
                    { id: '30', title: 'Lumpuhkan Ingatanku', artist: 'Geisha', thumbnail: 'https://i.ytimg.com/vi/oTJ4x1wY4n0/hqdefault.jpg' },
                    { id: '31', title: 'Kenangan Terindah', artist: 'SAMSONS', thumbnail: 'https://i.ytimg.com/vi/pTJ4x1wY4n0/hqdefault.jpg' },
                    { id: '32', title: 'Jiwa Yang Bersedih', artist: 'Ghea Indrawari', thumbnail: 'https://i.ytimg.com/vi/qTJ4x1wY4n0/hqdefault.jpg' },
                    { id: '33', title: 'bergema sampai selamanya', artist: 'Nadhif Basalamah', thumbnail: 'https://i.ytimg.com/vi/rTJ4x1wY4n0/hqdefault.jpg' },
                    { id: '34', title: 'Menua Bersamamu', artist: 'Shandy Pagalla Channel', thumbnail: 'https://i.ytimg.com/vi/sTJ4x1wY4n0/hqdefault.jpg' },
                    { id: '35', title: 'Tak Ingin Usai', artist: 'Keisya Levronka', thumbnail: 'https://i.ytimg.com/vi/tTJ4x1wY4n0/hqdefault.jpg' },
                    { id: '36', title: 'Mati-Matian', artist: 'Mahalini', thumbnail: 'https://i.ytimg.com/vi/uTJ4x1wY4n0/hqdefault.jpg' },
                ]
            },
            {
                id: 'baru_diputar',
                title: 'Baru diputar',
                type: 'grid',
                items: [
                    { id: '37', title: 'Cinta Merah Jambu', artist: 'LEK PANG', thumbnail: 'https://i.ytimg.com/vi/vTJ4x1wY4n0/hqdefault.jpg' },
                    { id: '38', title: 'Aku Dah Lupa', artist: 'Maman Fvndy', thumbnail: 'https://i.ytimg.com/vi/wTJ4x1wY4n0/hqdefault.jpg' },
                    { id: '39', title: 'Asmara Kerinduan (Remix)', artist: 'Meyda Rahma', thumbnail: 'https://i.ytimg.com/vi/xTJ4x1wY4n0/hqdefault.jpg' },
                    { id: '40', title: 'KUAN SOE LEKONES', artist: 'AITINA MUSIK', thumbnail: 'https://i.ytimg.com/vi/yTJ4x1wY4n0/hqdefault.jpg' },
                    { id: '41', title: 'Tabola Bale x Lampu Kaka', artist: 'Maman Fvndy', thumbnail: 'https://i.ytimg.com/vi/zTJ4x1wY4n0/hqdefault.jpg' },
                    { id: '42', title: 'Nan Ko Paham', artist: 'Maman Fvndy', thumbnail: 'https://i.ytimg.com/vi/ATJ4x1wY4n0/hqdefault.jpg' },
                    { id: '43', title: 'Cinta Dalam Duka', artist: 'Arief', thumbnail: 'https://i.ytimg.com/vi/BTJ4x1wY4n0/hqdefault.jpg' },
                    { id: '44', title: 'WEDI DOSA', artist: 'Missel Laura D', thumbnail: 'https://i.ytimg.com/vi/CTJ4x1wY4n0/hqdefault.jpg' },
                ]
            },
            {
                id: 'viral_tiktok',
                title: 'Viral TikTok',
                type: 'grid',
                items: [
                    { id: '45', title: 'Rindu Aku Rindu Kamu', artist: 'Maman Fvndy', thumbnail: 'https://i.ytimg.com/vi/DTJ4x1wY4n0/hqdefault.jpg' },
                    { id: '46', title: 'SOUND JJ PRESET FYP TIKTOK', artist: 'ARUL PCM', thumbnail: 'https://i.ytimg.com/vi/ETJ4x1wY4n0/hqdefault.jpg' },
                    { id: '47', title: 'DJ PALING ENAK', artist: 'Kristiwa Napu', thumbnail: 'https://i.ytimg.com/vi/FTJ4x1wY4n0/hqdefault.jpg' },
                    { id: '48', title: 'Jedag Jedug Preman', artist: 'Afrian Af', thumbnail: 'https://i.ytimg.com/vi/GTJ4x1wY4n0/hqdefault.jpg' },
                    { id: '49', title: '#jedagjedug', artist: 'Zachz Winner', thumbnail: 'https://i.ytimg.com/vi/HTJ4x1wY4n0/hqdefault.jpg' },
                    { id: '50', title: 'Tabola Bale', artist: 'Maman Fvndy', thumbnail: 'https://i.ytimg.com/vi/ITJ4x1wY4n0/hqdefault.jpg' },
                    { id: '51', title: 'DJ Raiso Ngapusi', artist: 'Adit Fvnky Rmx', thumbnail: 'https://i.ytimg.com/vi/JTJ4x1wY4n0/hqdefault.jpg' },
                    { id: '52', title: 'Tia Monika (Remix)', artist: 'Maman Fvndy', thumbnail: 'https://i.ytimg.com/vi/KTJ4x1wY4n0/hqdefault.jpg' },
                ]
            },
            {
                id: 'artis_populer',
                title: 'Artis Terpopuler Saat Ini',
                type: 'artist',
                items: [
                    { id: '53', title: 'Hati Yang Luka', type: 'Artis', thumbnail: 'https://i.ytimg.com/vi/LTJ4x1wY4n0/hqdefault.jpg' },
                    { id: '54', title: 'Tentang Rasa', type: 'Artis', thumbnail: 'https://i.ytimg.com/vi/MTJ4x1wY4n0/hqdefault.jpg' },
                    { id: '55', title: 'Bila Cinta Di Dusta', type: 'Artis', thumbnail: 'https://i.ytimg.com/vi/NTJ4x1wY4n0/hqdefault.jpg' },
                    { id: '56', title: 'Mencari Alasan', type: 'Artis', thumbnail: 'https://i.ytimg.com/vi/OTJ4x1wY4n0/hqdefault.jpg' },
                    { id: '57', title: 'Bersama Bintang', type: 'Artis', thumbnail: 'https://i.ytimg.com/vi/PTJ4x1wY4n0/hqdefault.jpg' },
                    { id: '58', title: 'Hanya Rindu', type: 'Artis', thumbnail: 'https://i.ytimg.com/vi/QTJ4x1wY4n0/hqdefault.jpg' },
                    { id: '59', title: 'Satu Nama Tetap Di Hati', type: 'Artis', thumbnail: 'https://i.ytimg.com/vi/RTJ4x1wY4n0/hqdefault.jpg' },
                    { id: '60', title: 'Keras Kepala', type: 'Artis', thumbnail: 'https://i.ytimg.com/vi/STJ4x1wY4n0/hqdefault.jpg' },
                ]
            },
            {
                id: 'hit_hari_ini',
                title: 'Hit terpopuler hari ini',
                type: 'grid',
                items: [
                    { id: '61', title: 'Anugerah Terindah', artist: 'Andmesh', thumbnail: 'https://i.ytimg.com/vi/TTJ4x1wY4n0/hqdefault.jpg' },
                    { id: '62', title: 'Rahasia Hati', artist: 'NIDJI', thumbnail: 'https://i.ytimg.com/vi/UTJ4x1wY4n0/hqdefault.jpg' },
                    { id: '63', title: 'Kehadiranmu', artist: 'Vagetoz', thumbnail: 'https://i.ytimg.com/vi/VTJ4x1wY4n0/hqdefault.jpg' },
                    { id: '64', title: 'Tujh Mein Rab Dikhta Hai', artist: 'Roop Kumar Rathod', thumbnail: 'https://i.ytimg.com/vi/WTJ4x1wY4n0/hqdefault.jpg' },
                    { id: '65', title: 'Nanti Kita Seperti Ini', artist: 'BATAS SENJA', thumbnail: 'https://i.ytimg.com/vi/XTJ4x1wY4n0/hqdefault.jpg' },
                    { id: '66', title: 'Satu Rasa Cinta', artist: 'Fendik Adella', thumbnail: 'https://i.ytimg.com/vi/YTJ4x1wY4n0/hqdefault.jpg' },
                    { id: '67', title: 'Sinarengan', artist: 'Denny Caknan', thumbnail: 'https://i.ytimg.com/vi/ZTJ4x1wY4n0/hqdefault.jpg' },
                    { id: '68', title: 'Bunga Abadi', artist: 'Rio Clappy', thumbnail: 'https://i.ytimg.com/vi/aUJ4x1wY4n0/hqdefault.jpg' },
                ]
            },
            {
                id: 'tiktok_playlist',
                title: 'Dibuat Untuk TikTok',
                type: 'grid',
                items: [
                    { id: '69', title: 'Playlist For TikTok Content', artist: 'DJ TikTok', thumbnail: 'https://i.ytimg.com/vi/bUJ4x1wY4n0/hqdefault.jpg' },
                    { id: '70', title: 'Garam Dan Madu', artist: 'Maman Fvndy', thumbnail: 'https://i.ytimg.com/vi/cUJ4x1wY4n0/hqdefault.jpg' },
                    { id: '71', title: 'Infinity', artist: 'Jaymes Young', thumbnail: 'https://i.ytimg.com/vi/dUJ4x1wY4n0/hqdefault.jpg' },
                    { id: '72', title: 'Playlist For TikTok', artist: 'TikTok Music', thumbnail: 'https://i.ytimg.com/vi/eUJ4x1wY4n0/hqdefault.jpg' },
                    { id: '73', title: 'Playlist For TikTok', artist: 'TikTok Music', thumbnail: 'https://i.ytimg.com/vi/fUJ4x1wY4n0/hqdefault.jpg' },
                    { id: '74', title: 'TikTok Playlist', artist: 'TikTokHub', thumbnail: 'https://i.ytimg.com/vi/gUJ4x1wY4n0/hqdefault.jpg' },
                    { id: '75', title: 'Playlist For TikTok', artist: 'TikTok Music', thumbnail: 'https://i.ytimg.com/vi/hUJ4x1wY4n0/hqdefault.jpg' },
                    { id: '76', title: 'TikTok Trap Beats Playlist', artist: 'TikTokHub', thumbnail: 'https://i.ytimg.com/vi/iUJ4x1wY4n0/hqdefault.jpg' },
                ]
            },
            {
                id: 'album_populer',
                title: 'Album dan single populer',
                type: 'grid',
                items: [
                    { id: '77', title: 'Baby (feat. Ludacris)', artist: 'Justin Bieber', thumbnail: 'https://i.ytimg.com/vi/kffacxfA7G4/hqdefault.jpg' },
                    { id: '78', title: 'Hotel California', artist: 'Eagles', thumbnail: 'https://i.ytimg.com/vi/BciS5krYL80/hqdefault.jpg' },
                    { id: '79', title: 'ANDAI TAK BERPISAH', artist: 'Rheina official', thumbnail: 'https://i.ytimg.com/vi/lUJ4x1wY4n0/hqdefault.jpg' },
                    { id: '80', title: 'Levitating', artist: 'Dua Lipa', thumbnail: 'https://i.ytimg.com/vi/TUVcZfQe-Kw/hqdefault.jpg' },
                    { id: '81', title: 'One Time', artist: 'Justin Bieber', thumbnail: 'https://i.ytimg.com/vi/CHVhwcOg6y8/hqdefault.jpg' },
                    { id: '82', title: 'I Wanna Dance with Somebody', artist: 'Whitney Houston', thumbnail: 'https://i.ytimg.com/vi/eH3giaIzONA/hqdefault.jpg' },
                    { id: '83', title: 'Shape of You', artist: 'Ed Sheeran', thumbnail: 'https://i.ytimg.com/vi/JGwWNGJdvx8/hqdefault.jpg' },
                    { id: '84', title: "You'll Be in My Heart", artist: 'NIKI', thumbnail: 'https://i.ytimg.com/vi/mUJ4x1wY4n0/hqdefault.jpg' },
                ]
            }
        ]
    };
}

function renderHomeSections(container, sections) {
    container.innerHTML = sections.map(section => {
        const isArtist = section.type === 'artist';
        const containerClass = section.type === 'horizontal' ? 'horizontal-scroll' : 'card-grid';
        
        const itemsHtml = section.items.map(item => {
            if (isArtist) {
                return `
                    <div class="artist-card" data-id="${item.id}" data-title="${item.title}">
                        <div class="artist-thumb">
                            <img src="${item.thumbnail}" alt="${item.title}" loading="lazy">
                        </div>
                        <div class="artist-name">${item.title}</div>
                        <div class="artist-type">${item.type}</div>
                    </div>
                `;
            }
            
            return `
                <div class="music-card" data-id="${item.id}" data-title="${item.title}" data-artist="${item.artist}" data-thumbnail="${item.thumbnail}">
                    <div class="card-thumb">
                        <img src="${item.thumbnail}" alt="${item.title}" loading="lazy">
                        <div class="card-overlay">
                            <div class="play-icon">
                                <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                                    <path d="M8 5v14l11-7z"/>
                                </svg>
                            </div>
                        </div>
                    </div>
                    <div class="card-info">
                        <div class="card-title">${item.title}</div>
                        <div class="card-artist">${item.artist}</div>
                    </div>
                </div>
            `;
        }).join('');
        
        return `
            <div class="section" data-type="${section.id.includes('podcast') ? 'podcast' : 'music'}">
                <div class="section-header">
                    <h2 class="section-title">${section.title}</h2>
                </div>
                <div class="${containerClass}">
                    ${itemsHtml}
                </div>
            </div>
        `;
    }).join('');
    
    // Add click handlers
    container.querySelectorAll('.music-card').forEach(card => {
        card.addEventListener('click', () => {
            const song = {
                id: card.dataset.id,
                title: card.dataset.title,
                artist: card.dataset.artist,
                thumbnail: card.dataset.thumbnail
            };
            playSong(song);
        });
    });
}

// ===== Categories =====
async function loadCategories() {
    try {
        // Fetch from API
        const response = await fetch(`${API_BASE_URL}/categories`);
        const data = await response.json();
        const categories = data.categories || [];
        
        elements.categoryGrid.innerHTML = categories.map(cat => `
            <div class="category-card" style="background: ${cat.color}" data-id="${cat.id}">
                <h3>${cat.name}</h3>
            </div>
        `).join('');
    } catch (error) {
        console.error('Error loading categories:', error);
        // Fallback to default categories
        const categories = [
            { id: 'made-for-you', name: 'Dibuat Untuk Kamu', color: '#8B5CF6' },
            { id: 'upcoming', name: 'Rilis Mendatang', color: '#10B981' },
            { id: 'new-releases', name: 'Rilis Baru', color: '#84CC16' },
            { id: 'ramadan', name: 'Ramadan', color: '#10B981' },
            { id: 'pop', name: 'Pop', color: '#3B82F6' },
            { id: 'indie', name: 'Indie', color: '#EC4899' },
            { id: 'indonesian', name: 'Musik Indonesia', color: '#EF4444' },
            { id: 'charts', name: 'Tangga Lagu', color: '#8B5CF6' },
            { id: 'podcast', name: 'Peringkat Podcast', color: '#1E3A8A' },
            { id: 'kpop', name: 'K-pop', color: '#EC4899' },
        ];
        
        elements.categoryGrid.innerHTML = categories.map(cat => `
            <div class="category-card" style="background: ${cat.color}" data-id="${cat.id}">
                <h3>${cat.name}</h3>
            </div>
        `).join('');
    }
}

// ===== Search =====
function setupSearch() {
    let debounceTimer;
    
    elements.searchInput.addEventListener('input', (e) => {
        clearTimeout(debounceTimer);
        const query = e.target.value.trim();
        
        if (query.length === 0) {
            elements.searchResults.innerHTML = '';
            return;
        }
        
        debounceTimer = setTimeout(() => {
            performSearch(query);
        }, 300);
    });
}

async function performSearch(query) {
    try {
        // Fetch from API
        const response = await fetch(`${API_BASE_URL}/search?query=${encodeURIComponent(query)}`);
        const data = await response.json();
        renderSearchResults(data.results || []);
    } catch (error) {
        console.error('Search error:', error);
        // Fallback to mock data
        const results = getMockSearchResults(query);
        renderSearchResults(results);
    }
}

function getMockSearchResults(query) {
    const allSongs = [];
    state.homeData?.sections.forEach(section => {
        if (section.items) {
            allSongs.push(...section.items);
        }
    });
    
    return allSongs.filter(song => 
        song.title.toLowerCase().includes(query.toLowerCase()) ||
        (song.artist && song.artist.toLowerCase().includes(query.toLowerCase()))
    ).slice(0, 10);
}

function renderSearchResults(results) {
    if (results.length === 0) {
        elements.searchResults.innerHTML = '<p style="padding: 16px; color: var(--text-secondary);">Tidak ada hasil ditemukan</p>';
        return;
    }
    
    elements.searchResults.innerHTML = results.map(song => `
        <div class="search-result-item" data-id="${song.id}" data-title="${song.title}" data-artist="${song.artist || ''}" data-thumbnail="${song.thumbnail}">
            <img src="${song.thumbnail}" alt="${song.title}">
            <div class="search-result-info">
                <h4>${song.title}</h4>
                <p>${song.artist || 'Artis'}</p>
            </div>
        </div>
    `).join('');
    
    // Add click handlers
    elements.searchResults.querySelectorAll('.search-result-item').forEach(item => {
        item.addEventListener('click', () => {
            const song = {
                id: item.dataset.id,
                title: item.dataset.title,
                artist: item.dataset.artist,
                thumbnail: item.dataset.thumbnail
            };
            playSong(song);
        });
    });
}

// ===== Player =====
function setupPlayer() {
    // Mini player controls
    document.getElementById('play-btn').addEventListener('click', togglePlay);
    document.getElementById('prev-btn').addEventListener('click', playPrevious);
    document.getElementById('next-btn').addEventListener('click', playNext);
    
    // Full player controls
    document.getElementById('full-play-btn').addEventListener('click', togglePlay);
    document.getElementById('full-prev-btn').addEventListener('click', playPrevious);
    document.getElementById('full-next-btn').addEventListener('click', playNext);
    document.getElementById('close-player').addEventListener('click', closeFullPlayer);
    
    // Open full player on mini player click
    elements.playerBar.addEventListener('click', (e) => {
        if (!e.target.closest('.control-btn')) {
            openFullPlayer();
        }
    });
    
    // Audio events
    elements.audioPlayer.addEventListener('timeupdate', updateProgress);
    elements.audioPlayer.addEventListener('ended', playNext);
    elements.audioPlayer.addEventListener('loadedmetadata', updateDuration);
}

async function playSong(song) {
    state.currentSong = song;
    state.isPlaying = true;
    
    // Update UI
    updatePlayerUI();
    
    // Show player bar
    elements.playerBar.classList.add('active');
    
    // Add to recently played
    await musicDB.addToRecentlyPlayed(song);
    
    // Update recently played list
    await loadRecentlyPlayed();
    
    // Simulate playing (in real app, set audio source)
    // elements.audioPlayer.src = song.streamUrl;
    // elements.audioPlayer.play();
    
    showToast(`Memutar: ${song.title}`);
}

function updatePlayerUI() {
    if (!state.currentSong) return;
    
    const { title, artist, thumbnail } = state.currentSong;
    
    // Mini player
    document.getElementById('player-thumb').src = thumbnail;
    document.getElementById('player-title').textContent = title;
    document.getElementById('player-artist').textContent = artist;
    
    // Full player
    document.getElementById('full-album-art').src = thumbnail;
    document.getElementById('full-title').textContent = title;
    document.getElementById('full-artist').textContent = artist;
    
    // Update play button
    updatePlayButton();
}

function updatePlayButton() {
    const playIcon = state.isPlaying 
        ? '<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><rect x="6" y="4" width="4" height="16"/><rect x="14" y="4" width="4" height="16"/></svg>'
        : '<svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg>';
    
    document.getElementById('play-btn').innerHTML = playIcon;
    document.getElementById('full-play-btn').innerHTML = playIcon.replace('width="24"', 'width="32"').replace('height="24"', 'height="32"');
}

function togglePlay() {
    if (!state.currentSong) {
        showToast('Pilih lagu untuk diputar');
        return;
    }
    
    state.isPlaying = !state.isPlaying;
    
    if (state.isPlaying) {
        elements.audioPlayer.play();
    } else {
        elements.audioPlayer.pause();
    }
    
    updatePlayButton();
}

function playPrevious() {
    if (state.queue.length === 0) return;
    
    state.currentIndex = (state.currentIndex - 1 + state.queue.length) % state.queue.length;
    playSong(state.queue[state.currentIndex]);
}

function playNext() {
    if (state.queue.length === 0) return;
    
    state.currentIndex = (state.currentIndex + 1) % state.queue.length;
    playSong(state.queue[state.currentIndex]);
}

function openFullPlayer() {
    if (!state.currentSong) return;
    elements.fullPlayer.classList.add('active');
}

function closeFullPlayer() {
    elements.fullPlayer.classList.remove('active');
}

function updateProgress() {
    const current = elements.audioPlayer.currentTime;
    const duration = elements.audioPlayer.duration;
    
    if (duration) {
        const percent = (current / duration) * 100;
        document.getElementById('progress-fill').style.width = `${percent}%`;
        document.getElementById('current-time').textContent = formatTime(current);
    }
}

function updateDuration() {
    const duration = elements.audioPlayer.duration;
    if (duration) {
        document.getElementById('duration').textContent = formatTime(duration);
    }
}

function formatTime(seconds) {
    if (isNaN(seconds)) return '0:00';
    
    const mins = Math.floor(seconds / 60);
    const secs = Math.floor(seconds % 60);
    return `${mins}:${secs.toString().padStart(2, '0')}`;
}

// ===== Liked Songs =====
async function loadLikedSongs() {
    try {
        state.likedSongs = await musicDB.getLikedSongs();
        elements.likedCount.textContent = state.likedSongs.length;
    } catch (error) {
        console.error('Error loading liked songs:', error);
    }
}

async function toggleLike(song) {
    try {
        const isLiked = await musicDB.isLiked(song.id);
        
        if (isLiked) {
            await musicDB.removeLikedSong(song.id);
            showToast('Dihapus dari lagu yang disukai');
        } else {
            await musicDB.addLikedSong(song);
            showToast('Ditambahkan ke lagu yang disukai');
        }
        
        await loadLikedSongs();
    } catch (error) {
        console.error('Error toggling like:', error);
    }
}

// ===== Recently Played =====
async function loadRecentlyPlayed() {
    try {
        state.recentlyPlayed = await musicDB.getRecentlyPlayed(8);
    } catch (error) {
        console.error('Error loading recently played:', error);
    }
}

// ===== Toast =====
function showToast(message) {
    elements.toast.textContent = message;
    elements.toast.classList.add('show');
    
    setTimeout(() => {
        elements.toast.classList.remove('show');
    }, 3000);
}

// ===== PWA =====
function setupPWA() {
    // Register service worker
    if ('serviceWorker' in navigator) {
        navigator.serviceWorker.register('sw.js').catch(err => {
            console.log('Service Worker registration failed:', err);
        });
    }
    
    // Install button
    let deferredPrompt;
    const installBtn = document.getElementById('install-btn');
    
    window.addEventListener('beforeinstallprompt', (e) => {
        e.preventDefault();
        deferredPrompt = e;
        installBtn.style.display = 'flex';
    });
    
    installBtn.addEventListener('click', async () => {
        if (deferredPrompt) {
            deferredPrompt.prompt();
            const { outcome } = await deferredPrompt.userChoice;
            
            if (outcome === 'accepted') {
                showToast('Aplikasi berhasil diinstall');
            }
            
            deferredPrompt = null;
        }
    });
}

// ===== Camera Button =====
document.getElementById('camera-btn')?.addEventListener('click', () => {
    showToast('Fitur kamera coming soon!');
});

// ===== Add Artist/Podcast =====
document.getElementById('add-artist')?.addEventListener('click', () => {
    showToast('Fitur tambah artis coming soon!');
});

document.getElementById('add-podcast')?.addEventListener('click', () => {
    showToast('Fitur tambah podcast coming soon!');
});

// ===== Liked Songs Click =====
document.getElementById('liked-songs')?.addEventListener('click', () => {
    if (state.likedSongs.length === 0) {
        showToast('Belum ada lagu yang disukai');
        return;
    }
    
    // Show liked songs playlist
    showToast(`Menampilkan ${state.likedSongs.length} lagu yang disukai`);
});
