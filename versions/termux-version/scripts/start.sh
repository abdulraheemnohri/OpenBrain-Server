#!/bin/bash
echo "Starting OpenBrain Server..."
# Install dependencies
pip install -r requirements.txt
# Start the FastAPI server
uvicorn backend.main:app --host 0.0.0.0 --port 8000
