#!/bin/bash

echo "[+] Installing PacketMiner dependencies..."

# Install system dependencies (Wireshark CLI tools)
if ! command -v editcap &> /dev/null; then
    echo "[+] Installing Wireshark CLI tools..."
    sudo apt update && sudo apt install -y wireshark
else
    echo "[✓] editcap found, skipping installation."
fi

# Create a virtual environment in the project root
if [ -f "venv/bin/activate" ]; then
    echo "[✓] Virtual environment found. Activating..."
    source venv/bin/activate
else
    echo "[!] Virtual environment not found. Creating one..."
    python3 -m venv venv
    source venv/bin/activate
fi

# Ensure requirements.txt exists
if [ ! -f "requirements.txt" ]; then
    echo "[!] requirements.txt not found! Creating one..."
    echo "scapy" > requirements.txt
fi

# Install Python dependencies
pip install --upgrade pip
pip install -r requirements.txt

echo "[+] Installation complete! Run 'packetminer' to start the tool."