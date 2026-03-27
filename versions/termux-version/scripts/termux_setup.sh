#!/data/data/com.termux/files/usr/bin/bash
echo "Installing ExpertAI Platform for Termux..."
pkg update && pkg upgrade -y
pkg install python git clang make libjpeg-turbo -y
pip install --upgrade pip
pip install -r requirements.txt
# Termux-specific torch/transformers often require manual wheel selection or specialized builds,
# but we stick to the provided requirements.txt.
echo "Termux Installation Complete. Start with 'bash scripts/start.sh'"
