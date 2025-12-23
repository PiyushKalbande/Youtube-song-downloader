#!/usr/bin/env bash
#ffmpeg
apt-get update && apt-get install -y ffmpeg
pip install -r requirements.txt && apt-get update && apt-get install -y nodejs