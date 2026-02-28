#!/usr/bin/env python3
"""
Startup script for Web Music Application
Starts both backend and serves frontend
"""

import subprocess
import sys
import os
import webbrowser
import time
import signal

def print_banner():
    print("""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║           SANN404 FORUM - Web Music v2.3.0                  ║
║                                                              ║
║              Sistem Informasi & Pengembangan                 ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
    """)

def install_dependencies():
    """Install Python dependencies"""
    print("📦 Installing dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "backend/requirements.txt"])
        print("✅ Dependencies installed successfully\n")
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        sys.exit(1)

def start_backend():
    """Start FastAPI backend"""
    print("🚀 Starting backend server...")
    print("📍 Backend URL: http://localhost:8000")
    print("📍 API Docs: http://localhost:8000/docs\n")
    
    try:
        # Change to backend directory
        os.chdir('backend')
        
        # Start uvicorn
        process = subprocess.Popen([
            sys.executable, "-m", "uvicorn", 
            "main:app", 
            "--host", "0.0.0.0", 
            "--port", "8000",
            "--reload"
        ])
        
        return process
    except Exception as e:
        print(f"❌ Failed to start backend: {e}")
        sys.exit(1)

def open_browser():
    """Open browser after delay"""
    time.sleep(3)
    print("🌐 Opening browser...")
    webbrowser.open('http://localhost:8000')

def signal_handler(sig, frame):
    """Handle Ctrl+C"""
    print("\n\n👋 Shutting down Web Music...")
    print("Terima kasih telah menggunakan aplikasi ini!")
    sys.exit(0)

def main():
    print_banner()
    
    # Setup signal handler
    signal.signal(signal.SIGINT, signal_handler)
    
    # Check if running from correct directory
    if not os.path.exists('backend/main.py'):
        print("❌ Error: Please run this script from the project root directory")
        sys.exit(1)
    
    # Install dependencies
    install_dependencies()
    
    # Start backend
    backend_process = start_backend()
    
    # Open browser
    open_browser()
    
    print("\n" + "="*60)
    print("✅ Web Music is running!")
    print("="*60)
    print("\nTekan Ctrl+C untuk menghentikan\n")
    
    try:
        # Wait for backend process
        backend_process.wait()
    except KeyboardInterrupt:
        signal_handler(None, None)

if __name__ == "__main__":
    main()
