# ExpertAI Platform - Mesh Network Version

This version enables a decentralized, distributed AI system by connecting multiple devices into one network.

## Features
- **Node Registry**: Register multiple devices (Android phones, Laptops, Servers) as AI nodes.
- **Distributed Experts**: Dispatch tasks across the network to specialized nodes for memory optimization.
- **Load Balancing**: Distribute the AI workload among available nodes for performance.

## Installation

### Router Node (Main Server)
1. Clone the repository
2. Run `bash scripts/start.sh`

### Worker Node (Expert Worker)
1. Register with the Router node (Mock)
2. Run the specialized expert model for the worker.

### Quick Start
Access the dashboard at `http://localhost:8000`. The Mesh Network version will automatically dispatch tasks to available remote nodes before local inference.
