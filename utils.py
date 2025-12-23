import os
import time

TEMP_FOLDER = "temp"
MAX_AGE = 60 * 60  # 1 hour in seconds

def cleanup_temp():
    now = time.time()

    if not os.path.exists(TEMP_FOLDER):
        return

    for file in os.listdir(TEMP_FOLDER):
        path = os.path.join(TEMP_FOLDER, file)
        try:
            if os.path.isfile(path):
                if now - os.path.getmtime(path) > MAX_AGE:
                    os.remove(path)
        except Exception:
            pass
