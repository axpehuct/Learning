import os

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)

ensure_dir(f"D:\\hi")
ensure_dir(f"D:\\hi")