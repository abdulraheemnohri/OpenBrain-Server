@echo off
echo ====================================================
echo       ExpertAI Platform - Interactive Installer
echo ====================================================
echo Select the version you want to install:
echo 1) Simple (Baseline Expert AI + Dashboard)
echo 2) Self-Evolving (Auto Plugin Discovery + Pattern Learning)
echo 3) Mesh Network (Distributed AI Nodes + Load Balancing)
echo 4) Custom (Select individual features)
set /p version_choice="Enter choice [1-4]: "

if "%version_choice%"=="1" (
    echo Installing Simple Version...
    set SRC_DIR=versions/simple-version
) else if "%version_choice%"=="2" (
    echo Installing Self-Evolving Version...
    set SRC_DIR=versions/self-evolving-version
) else if "%version_choice%"=="3" (
    echo Installing Mesh Network Version...
    set SRC_DIR=versions/mesh-network-version
) else (
    echo Invalid choice. Exiting.
    pause
    exit /b
)

xcopy /E /Y %SRC_DIR%\* .\
echo Installation complete. Starting server...
call scripts\start.bat
pause
