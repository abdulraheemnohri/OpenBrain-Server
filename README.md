# ExpertAI Platform - Multi-Version Repository

Welcome to the ExpertAI Platform repository. This project is organized into four distinct versions to suit different hosting requirements and performance goals.

## 🧠 Core Concept

The ExpertAI Platform is built on a modular **Expert Division (MoE)** architecture. Instead of running a massive 27B parameter model, the system divides the knowledge into smaller, specialized "experts". A lightweight router model (300M) analyzes your query and activates only the necessary expert for that specific task.

### Expert Model Division Diagram
```text
          27B Knowledge Base
                   │
                   ▼
          Knowledge Distillation
                   │
    ┌──────────────┼──────────────┐
    ▼              ▼              ▼
Chat Expert    Code Expert    Math Expert
   (3B)           (4B)           (3B)
    │              │              │
    └──────┬───────┴──────┬───────┘
           ▼              ▼
    Reasoning Expert  Translation Expert
         (4B)            (3B)
                 │
                 ▼
            Router Model
               (300M)
```

### Routing Logic
1. **User Query Received**: "Write a python script to scrape a website."
2. **Analysis**: The Router Model detects the "programming" task.
3. **Activation**: The system activates the **Code Expert** only.
4. **Benefit**:
   - ✔ **Low RAM Usage**: Only the 4B model runs, not the full 27B.
   - ✔ **Faster Response**: Specialized models provide quicker inference.
   - ✔ **Low-Device Friendly**: Optimized for Termux, Laptops, and IoT.

---

## 🚀 Full Project Details & Features

ExpertAI is a modular, open-source platform that enables you to host your own AI experts locally or in a distributed mesh network.

### Core Features:
- **Expert Division (MoE)**: Routing system that selects specialized models (Chat, Code, Math, etc.) based on user tasks.
- **OpenAI-compatible API**: Connect existing tools like OpenClaw, LangChain, and more.
- **Admin Dashboard**: Real-time server monitoring, logs, and advanced analytics.
- **Plugin System**: Modular tools for web searching, file reading, and more.
- **Cross-Platform Support**: Optimized scripts for Linux, Windows, and Termux.
- **Developer SDKs**: Official Python and JavaScript libraries for rapid integration.

---

## Project Versions & Installation

### 1. [Simple Version](./versions/simple-version)
**Baseline Implementation**
- **Features**: OpenAI API, Expert AI routing, Dashboard, Plugin support.
- **Installation**:
  ```bash
  cd versions/simple-version
  bash scripts/start.sh (Linux) or scripts/start.bat (Windows)
  ```

### 2. [Self-Evolving Version](./versions/self-evolving-version)
**Automated Growth**
- **Features**: Dynamic tool discovery, Expert pattern learning, Self-optimization.
- **Installation**:
  ```bash
  cd versions/self-evolving-version
  bash scripts/start.sh (Linux) or scripts/start.bat (Windows)
  ```

### 3. [Mesh Network Version](./versions/mesh-network-version)
**Decentralized AI**
- **Features**: Node registry, Distributed experts, Load balancing across multiple devices.
- **Installation**:
  ```bash
  cd versions/mesh-network-version
  bash scripts/start.sh (Linux) or scripts/start.bat (Windows)
  ```

### 4. [Termux Version](./versions/termux-version)
**Mobile Optimized**
- **Features**: Specialized setup for Android Termux with optimized dependencies and library support.
- **Installation (Termux)**:
  ```bash
  cd versions/termux-version
  bash scripts/termux_setup.sh
  ```

---

## Repository Link
[https://github.com/abdulraheemnohri/OpenBrain-Server](https://github.com/abdulraheemnohri/OpenBrain-Server)

## License
MIT
