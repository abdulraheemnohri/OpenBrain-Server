# ExpertAI Platform - Simple Version

This is the baseline implementation of the ExpertAI Platform, designed for local hosting with a powerful feature set.

## Features
- **Expert Division (MoE)**: Routing system that selects specialized models (Chat, Code, Math, etc.) based on user tasks.
- **OpenAI-compatible API**: Standardized endpoint for integration with existing tools like OpenClaw and LangChain.
- **Admin Dashboard**: Real-time server monitoring, logs, and advanced analytics.
- **Plugin System**: Support for modular tools like `web_search` and `file_reader`.

## Installation

### Linux
1. Clone the repository
2. Run `bash scripts/start.sh`

### Windows
1. Clone the repository
2. Run `scripts/start.bat`

### Quick Start
Access the dashboard at `http://localhost:8000`.

## Documentation
- [API Reference](docs/api.md)
- [Architecture Guide](docs/architecture.md)
