# OpenBrain Server

**Self-Hosted AI Platform with API, Dashboard, and Multi-System Support**

OpenBrain is an open-source AI server designed to host Large Language Models (LLMs) locally, provide an OpenAI-compatible API, and offer a powerful admin dashboard for monitoring and management.

## Features
- **OpenAI-compatible API**: Connect your favorite AI tools like OpenClaw, LangChain, and more.
- **Admin Dashboard**: Manage API keys, view real-time logs, and monitor usage analytics.
- **Local AI Hosting**: Run Qwen models (27B GPTQ) on your hardware.
- **Cross-Platform**: Works on Windows, Linux, and Termux (Android).
- **Keyword Routing**: Automatically categorizes queries for specialized handling.

## Quick Start
1. Clone the repository:
   ```bash
   git clone https://github.com/openbrain/openbrain-server.git
   cd openbrain-server
   ```
2. Run the startup script for your platform:
   - **Linux**: `bash scripts/start.sh`
   - **Windows**: `scripts/start.bat`
   - **Termux**: `bash scripts/termux_setup.sh`

3. Access the Dashboard:
   - Open `http://localhost:8000` in your browser.

## Documentation
- [Installation Guide](docs/install.md)
- [API Reference](docs/api.md)
- [Architecture](docs/architecture.md)

## License
MIT License
