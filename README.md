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

---

## 🚀 Feature Matrix

| Feature | Simple | Self-Evolving | Mesh Network | Termux |
| :--- | :---: | :---: | :---: | :---: |
| **OpenAI-Compatible API** | ✅ | ✅ | ✅ | ✅ |
| **Admin Dashboard** | ✅ | ✅ | ✅ | ✅ |
| **Expert AI Routing** | ✅ | ✅ | ✅ | ✅ |
| **Plugin System** | ✅ | ✅ | ✅ | ✅ |
| **Tool Calling** | ✅ | ✅ | ✅ | ✅ |
| **Analytics & Logs** | ✅ | ✅ | ✅ | ✅ |
| **Settings Persistence** | ✅ | ✅ | ✅ | ✅ |
| **Auto Plugin Discovery** | ❌ | ✅ | ❌ | ❌ |
| **Task Pattern Learning** | ❌ | ✅ | ❌ | ❌ |
| **Distributed Nodes** | ❌ | ❌ | ✅ | ❌ |
| **Termux Optimization** | ❌ | ❌ | ❌ | ✅ |

---

## 🛠 Project Versions & Installation

### 1. [Simple Version](./versions/simple-version)
**Baseline Implementation**
- **Features**: OpenAI API, Expert AI routing, Dashboard, Plugin support, Persistent Settings.

### 2. [Self-Evolving Version](./versions/self-evolving-version)
**Automated Growth**
- **Features**: Dynamic tool discovery, Expert pattern learning, Self-optimization.

### 3. [Mesh Network Version](./versions/mesh-network-version)
**Decentralized AI**
- **Features**: Node registry, Distributed experts, Load balancing across multiple devices.

### 4. [Termux Version](./versions/termux-version)
**Mobile Optimized**
- **Features**: Specialized setup for Android Termux with optimized dependencies and mobile-friendly library support.

---

## 🔗 Quick Start

1. **Clone the repository**:
   ```bash
   git clone https://github.com/abdulraheemnohri/OpenBrain-Server.git
   cd OpenBrain-Server
   ```
2. **Run the Interactive Installer**:
   - **Linux/Termux**: `bash install.sh`
   - **Windows**: `install.bat`

---

## Repository Link
[https://github.com/abdulraheemnohri/OpenBrain-Server](https://github.com/abdulraheemnohri/OpenBrain-Server)

## License
MIT
