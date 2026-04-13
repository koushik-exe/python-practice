import os
import shutil
import hashlib
from datetime import datetime

# 📂 Paths
SOURCE_FOLDER = r"C:\Users\ckous\Desktop\Messy"
DEST_FOLDER = r"C:\Users\ckous\Desktop\Organizer"

LOG_FILE = os.path.join(DEST_FOLDER, "organizer_log.txt")

# 📁 Categories
file_types = {
    "Images": [".jpg",".jpeg",".png",".webp",".bmp",".gif",".tiff",".tif",".heic",".heif",".svg",".raw",".cr2",".nef",".arw",".dng"],
    "Videos": [".mp4",".mkv",".avi",".mov",".wmv",".flv",".webm",".mpeg",".mpg",".3gp",".m4v",".ts",".vob"],
    "Audio": [".mp3",".wav",".aac",".flac",".ogg",".opus",".m4a",".wma",".aiff",".alac"],
    "Documents": [".pdf",".txt",".doc",".docx",".odt",".xls",".xlsx",".ods",".ppt",".pptx",".odp",".csv",".rtf",".md",".epub"],
    "Archives": [".zip",".rar",".7z",".tar",".gz",".bz2",".xz",".iso"],
    "Code": [".py",".js",".html",".css",".java",".c",".cpp",".json",".xml",".yml",".yaml",".sh",".bat"]
}

MONTHS = {
    1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",
    7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"
}

hash_map = {}

# 🔐 SHA-256 FULL HASH
def get_file_hash(filepath):
    hasher = hashlib.sha256()
    with open(filepath, 'rb') as f:
        while chunk := f.read(8192):
            hasher.update(chunk)
    return hasher.hexdigest()

# 🛡️ Safe filename
def get_unique_filename(folder, filename):
    name, ext = os.path.splitext(filename)
    counter = 1
    new_name = filename
    while os.path.exists(os.path.join(folder, new_name)):
        new_name = f"{name}_{counter}{ext}"
        counter += 1
    return new_name

# 📸 EXIF date
def get_image_date(filepath):
    try:
        from PIL import Image
        from PIL.ExifTags import TAGS
        image = Image.open(filepath)
        exif = image._getexif()
        if exif:
            for tag, value in exif.items():
                if TAGS.get(tag) == "DateTimeOriginal":
                    return datetime.strptime(value, "%Y:%m:%d %H:%M:%S")
    except:
        pass
    return None

# 📅 Get best date
def get_file_date(filepath):
    ext = os.path.splitext(filepath)[1].lower()

    if ext in file_types["Images"]:
        exif_date = get_image_date(filepath)
        if exif_date:
            return exif_date

    return datetime.fromtimestamp(os.path.getmtime(filepath))

# 📁 Category
def get_category(file):
    ext = os.path.splitext(file)[1].lower()
    for category, exts in file_types.items():
        if ext in exts:
            return category
    return "Others"

# 🧾 Log
def log(msg):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(msg + "\n")

# 🔥 STEP 1: Scan Organizer (IMPORTANT FIX)
def scan_existing_files():
    print("🔍 Scanning Organizer for existing files...")
    for root, dirs, files in os.walk(DEST_FOLDER):
        for file in files:
            file_path = os.path.join(root, file)

            # Skip log file
            if file_path == LOG_FILE:
                continue

            try:
                file_hash = get_file_hash(file_path)
                hash_map[file_hash] = file_path
            except:
                pass

    print(f"✅ Loaded {len(hash_map)} existing files")

# 🚀 Main
def organize():
    moved = 0
    duplicates = 0

    # 🔥 Load existing hashes
    scan_existing_files()

    for root, dirs, files in os.walk(SOURCE_FOLDER):
        for file in files:
            file_path = os.path.join(root, file)

            try:
                file_hash = get_file_hash(file_path)
                category = get_category(file)
                date = get_file_date(file_path)

                year = str(date.year)
                month = MONTHS[date.month]

                normal_folder = os.path.join(DEST_FOLDER, category, year, month)
                duplicate_folder = os.path.join(DEST_FOLDER, "Duplicates", category, year, month)

                # 🔁 Duplicate check (NOW WORKS ACROSS ORGANIZER)
                if file_hash in hash_map:
                    os.makedirs(duplicate_folder, exist_ok=True)

                    unique_name = get_unique_filename(duplicate_folder, file)
                    shutil.move(file_path, os.path.join(duplicate_folder, unique_name))

                    msg = f"Duplicate: {file}"
                    print(msg)
                    log(msg)
                    duplicates += 1
                    continue

                hash_map[file_hash] = file

                # 📂 Move normal
                os.makedirs(normal_folder, exist_ok=True)

                unique_name = get_unique_filename(normal_folder, file)
                shutil.move(file_path, os.path.join(normal_folder, unique_name))

                msg = f"Moved: {file} → {category}/{year}/{month}"
                print(msg)
                log(msg)
                moved += 1

            except Exception as e:
                msg = f"Error: {file} → {e}"
                print(msg)
                log(msg)

    summary = f"\n✅ DONE! Moved: {moved} | Duplicates: {duplicates}"
    print(summary)
    log(summary)

# ▶ Run
organize()