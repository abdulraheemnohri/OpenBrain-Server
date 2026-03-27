# Installation Guide

## Requirements
- Python 3.9+
- CUDA-enabled GPU (optional, for acceleration)
- At least 8GB RAM (16GB+ recommended for 27B model)

## Windows 10+
1. Clone the repository: `git clone ...`
2. Run `scripts/start.bat`

## Linux (Ubuntu / Debian / Arch)
1. Clone the repository
2. Run `bash scripts/start.sh`

## Termux (Android)
1. Update packages: `pkg update && pkg upgrade`
2. Run `bash scripts/termux_setup.sh`
3. Start server: `uvicorn backend.main:app`
