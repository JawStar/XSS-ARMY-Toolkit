#!/bin/bash
echo "[*] Running setup for XSS ARMY Toolkit..."
apt update -y && apt install -y python3 python3-pip ruby git golang
pip3 install -r requirements.txt
chmod +x tools/dalfox/dalfox
chmod +x tools/xspear/xspear.rb
echo "[+] Setup complete. Run the toolkit using: bash launcher.sh"
