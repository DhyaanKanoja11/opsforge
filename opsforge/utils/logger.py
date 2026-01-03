import datetime
import os

LOG_PATH = os.path.join("opsforge", "storage", "logs.txt")

def log(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] {message}\n"

    with open(LOG_PATH, "a") as f:
        f.write(entry)
