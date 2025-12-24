#!/usr/bin/env bash
# Exit on error
set -o errexit

pip install -r requirements.txt

# Download Linux FFmpeg (kyunki Render Linux hai, Windows .exe nahi chalega)
mkdir -p ffmpeg_bin
cd ffmpeg_bin
curl -L johnvansickle.com | tar xJ --strip-components=1
chmod +x ffmpeg
cd ..
