import os
import shutil
from datetime import datetime

# 📂 ONLY duplicate folder
SOURCE = r"C:\Users\ckous\Desktop\Organizer\Duplicates"

# 📅 Months
MONTHS = {
    1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",
    7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"
}

# 📁 Categories (your improved version)
file_types = {
    "Images": [".jpg",".jpeg",".png",".webp",".bmp",".gif",".tiff",".tif",".heic",".heif",".svg"],
    "RAW_Images": [".raw",".cr2",".nef",".arw",".dng"],
    "Videos": [".mp4",".mkv",".avi",".mov",".wmv",".flv",".webm",".mpeg",".mpg",".3gp",".m4v",".ts",".vob"],
    "Audio": [".mp3",".wav",".aac",".flac",".ogg",".opus",".m4a",".wma",".aiff",".alac"],
    "Documents": [".pdf",".txt",".doc",".docx",".odt",".xls",".xlsx",".ods",".ppt",".pptx",".odp",".csv",".rtf",".md",".epub"],
    "Archives": [".zip",".rar",".7z",".tar",".gz",".bz2",".xz",".iso"],
    "Code": [".py",".js",".html",".css",".java",".c",".cpp",".json",".xml",".yml",".yaml",".sh",".bat"]
}

# 📁 detect category
def get_category(file):
    ext = os.path.splitext(file)[1].lower()
    for cat, exts in file_types.items():
        if ext in exts:
            return cat
    return "Others"

# 📅 modified date
def get_date(path):
    return datetime.fromtimestamp(os.path.getmtime(path))

# 🔁 safe filename
def safe_name(folder, filename):
    name, ext = os.path.splitext(filename)
    counter = 1
    new_name = filename

    while os.path.exists(os.path.join(folder, new_name)):
        new_name = f"{name}_{counter}{ext}"
        counter += 1

    return new_name

# 🚀 main logic
def fix_duplicates():
    moved = 0
    skipped = 0

    for root, dirs, files in os.walk(SOURCE, topdown=False):
        for file in files:
            old_path = os.path.join(root, file)

            try:
                cat = get_category(file)
                date = get_date(old_path)

                year = str(date.year)
                month = MONTHS[date.month]

                target_folder = os.path.join(SOURCE, cat, year, month)
                os.makedirs(target_folder, exist_ok=True)

                new_file = safe_name(target_folder, file)
                new_path = os.path.join(target_folder, new_file)

                # already correct place
                if os.path.abspath(old_path) == os.path.abspath(new_path):
                    skipped += 1
                    continue

                shutil.move(old_path, new_path)

                print(f"✅ MOVED: {file} → {cat}/{year}/{month}")
                moved += 1

            except Exception as e:
                print(f"❌ ERROR: {file} → {e}")

    print("\n🎯 FINAL RESULT")
    print(f"✔ Moved: {moved}")
    print(f"⏭ Skipped: {skipped}")

# ▶ RUN
fix_duplicates()