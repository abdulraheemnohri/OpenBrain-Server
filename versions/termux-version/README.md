# ExpertAI Platform - Termux Optimized Version

This version is specifically tailored for running ExpertAI on Android devices via Termux. It includes optimized setup scripts and considerations for mobile hardware.

## Features
- **Mobile Optimized**: Uses specialized setup for Termux environments.
- **Resource Efficient**: Encourages the use of smaller, 4-bit quantized models suitable for mobile RAM.
- **Full ExpertAI Suite**: Includes the Dashboard, OpenAI-compatible API, and Plugin system.

## Installation (Termux)

1. **Install Termux** from F-Droid or GitHub.
2. **Clone the repository**:
   ```bash
   git clone https://github.com/abdulraheemnohri/OpenBrain-Server.git
   cd OpenBrain-Server
   ```
3. **Run the Installer**:
   - You can use the root installer: `bash install.sh` and select option 4.
   - Or run the setup directly:
     ```bash
     cd versions/termux-version
     bash scripts/termux_setup.sh
     ```
4. **Start the Server**:
   ```bash
   bash scripts/start.sh
   ```

## Optimization Tips for Termux
- Use models in **GGUF** or **GPTQ-Int4** format to save RAM.
- Limit `max_tokens` to prevent long processing times on mobile CPUs.
- Keep the device plugged in during long inference tasks to prevent battery drain.
