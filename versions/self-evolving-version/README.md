# ExpertAI Platform - Self-Evolving Version

This version focuses on automated growth and self-optimization of the ExpertAI Platform.

## Features
- **Dynamic Tool Discovery**: Automatically identifies and integrates new plugins.
- **Expert Learning**: Adapts the routing engine based on success/failure feedback from tasks.
- **Self-Optimization**: Analyzes performance logs to suggest configuration improvements.

## Installation

### Linux
1. Clone the repository
2. Run `bash scripts/start.sh`

### Windows
1. Clone the repository
2. Run `scripts/start.bat`

### Quick Start
Access the dashboard at `http://localhost:8000`.

## Evolution Engine
The evolution engine starts automatically and begins monitoring for new tools in the `plugins/` directory and learning task patterns to improve routing over time.
