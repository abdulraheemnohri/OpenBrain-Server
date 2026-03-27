#!/bin/bash

echo "===================================================="
echo "      ExpertAI Platform - Interactive Installer     "
echo "===================================================="
echo "Select the version you want to install:"
echo "1) Simple (Baseline Expert AI + Dashboard)"
echo "2) Self-Evolving (Auto Plugin Discovery + Pattern Learning)"
echo "3) Mesh Network (Distributed AI Nodes + Load Balancing)"
echo "4) Termux Optimized (Complete Android Support + Packages)"
echo "5) Custom (Select individual features)"
read -p "Enter choice [1-5]: " version_choice

case $version_choice in
    1)
        echo "Installing Simple Version..."
        SRC_DIR="versions/simple-version"
        ;;
    2)
        echo "Installing Self-Evolving Version..."
        SRC_DIR="versions/self-evolving-version"
        ;;
    3)
        echo "Installing Mesh Network Version..."
        SRC_DIR="versions/mesh-network-version"
        ;;
    4)
        echo "Installing Termux Version..."
        SRC_DIR="versions/termux-version"
        # Run Termux-specific setup
        bash $SRC_DIR/scripts/termux_setup.sh
        ;;
    5)
        echo "Custom Installation... (Defaulting to Simple for now)"
        SRC_DIR="versions/simple-version"
        ;;
    *)
        echo "Invalid choice. Exiting."
        exit 1
        ;;
esac

# Copy selected version to the root for operation
cp -rf $SRC_DIR/* ./
echo "Installation complete. Starting server..."
bash scripts/start.sh
