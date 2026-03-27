#!/data/data/com.termux/files/usr/bin/bash
echo "Setting up OpenBrain for Termux..."
pkg update && pkg upgrade -y
pkg install python git -y
pip install -r requirements.txt
echo "Setup complete. Start with 'python -m uvicorn backend.main:app'"
