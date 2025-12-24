#!/usr/bin/env bash
set -o errexit

# 1. Python dependencies
pip install -r requirements.txt

# 2. FFmpeg setup (2025 reliable link)
echo "Installing FFmpeg..."
mkdir -p ffmpeg_bin
# Download direct binary instead of tarball to avoid extraction errors
curl -L github.com | gunzip > ffmpeg_bin/ffmpeg

# 3. Permissions
chmod +x ffmpeg_bin/ffmpeg

echo "Build Successful!"
