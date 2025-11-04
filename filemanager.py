import os
import shutil

homepath = "D:/Code/Coding/automation"  # later, it'll be user-input-based variable
if not os.path.exists(homepath):
    print(f"ERROR: Path '{homepath}' doesn't exist...")
    exit()

files = os.listdir(homepath)
if not files:
    print(f"Aww, no files to process in '{homepath}'...")
    exit()

print(f"Alright, starting to organize {len(files)} items in '{homepath}'...")
for filename in files:
    files_source_path = os.path.join(homepath, filename)
    if os.path.isdir(files_source_path):
        print(f"Meow! Skipping the directory: '{filename}'...")
        continue

    extension = os.path.splitext(filename)[1].lower()
    if extension in [
        ".jpg",
        ".jpeg",
        ".png",
        ".gif",
        ".tif",
        ".tiff",
        ".bmp",
        ".webp",
        ".heif",
        ".heic",
        ".svg",
        ".eps",
        ".ai",
        ".psd",
        ".raw",
        ".cr2",
        ".nef",
        ".orf",
        ".sr2",
        ".dng",
    ]:
        target_dir_name = "Photos"
    elif extension in [
        ".html",
        ".htm",
        ".css",
        ".js",
        ".ts",
        ".php",
        ".aspx",
        ".c",
        ".cpp",
        ".cxx",
        ".cc",
        ".h",
        ".hpp",
        ".java",
        ".class",
        ".cs",
        ".go",
        ".swift",
        ".py",
        ".rb",
        ".rs",
        ".kt",
        ".sh",
        ".bat",
        ".ps1",
        ".vbs",
        ".json",
        ".xml",
        ".yml",
        ".yaml",
        ".sql",
        ".md",
        ".exe",
        ".bin",
        ".dll",
        ".so",
        ".jar",
        ".o",
        ".obj",
        ".sln",
    ]:
        target_dir_name = "Coding"
    elif extension in [
        ".pdf",
        ".docx",
        ".txt",
        ".md",
    ]:
        target_dir_name = "Documents"
    elif extension in [
        ".zip",
        ".rar",
        ".7z",
    ]:
        target_dir_name = "Archives"
    elif extension in [
        ".mp4",
        ".mov",
        ".avi",
        ".mkv",
        ".wmv",
        ".flv",
        ".webm",
        ".mpg",
        ".mpeg",
        ".3gp",
        ".m4v",
        ".mts",
        ".m2ts",
        ".ts",
        ".asf",
        ".ogv",
        ".ogg",
        ".vob",
        ".qt",
        ".rm",
        ".f4v",
        ".swf",
        ".dvr-ms",
        ".mod",
        ".amv",
        ".mxf",
        ".nsv",
        ".rrc",
        ".yuv",
    ]:
        target_dir_name = "Videos"
    elif extension in [
        ".exe",
    ]:
        target_dir_name = "Coding"
    else:
        print(f"OOPS, skipping the file: {filename} (unrecognized extension)...")
        continue

    target_dir_path = os.path.join(homepath, target_dir_name)
    if not os.path.exists(target_dir_path):
        os.mkdir(target_dir_path)
        print(f"Hint: Created folder: '{target_dir_path}'...")

    try:
        shutil.move(files_source_path, target_dir_path)
        print(f"Moved '{filename}' to '{target_dir_name}'... OK")
    except Exception as e:
        print(f"ERROR: Problem while moving '{filename}': {e}...")

print("\nFile organization completed!")
