#!/data/data/com.termux/files/usr/bin/bash
pkg update -y && pkg install -y python git
cd ~
rm -rf termux-cli-launcher
git clone https://github.com/yourusername/termux-cli-launcher.git
cd termux-cli-launcher
python main.py
