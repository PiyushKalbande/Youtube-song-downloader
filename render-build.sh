#!/usr/bin/env bash
set -o errexit

# 1. Python dependencies install karein
pip install -r requirements.txt

# 2. FFmpeg Static Binary (Direct Link) download karein
echo "Downloading FFmpeg..."
mkdir -p ffmpeg_bin

# Direct URL for Linux 64-bit static build
curl -L "johnvansickle.com" | tar xJ --strip-components=1 -C ./ffmpeg_bin

# 3. Make sure the binary is executable
chmod +x ffmpeg_bin/ffmpeg
