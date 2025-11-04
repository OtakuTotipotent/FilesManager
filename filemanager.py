import os
import shutil

homepath = "D:/Code/Coding/automation"
if not os.path.exists(homepath):
    print(f"ERROR: Path '{homepath}' doesn't exist...")
    exit()

files = os.listdir(homepath)
