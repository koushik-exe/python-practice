import os
import shutil
import hashlib
from datetime import datetime

BASE_FOLDER = r"C:\Users\ckous\Desktop\Organizer"

file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".webp"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Audio": [".mp3", ".wav", ".opus"],
    "Documents": [".pdf", ".txt", ".docx", ".xlsx", ".csv", ".pptx", ".ppt"],
}

MONTHS = {
    1: "January", 2: "February", 3: "March", 4: "April",
    5: "May", 6: "June", 7: "July", 8: "August",
    9: "September", 10: "October", 11: "November", 12: "December"
}

hash_map = {}

def get_file_hash(filepath):
    hasher = hashlib.md5()
    with open(filepath, 'rb') as f:
        while chunk := f.read(4096):
            hasher.update(chunk)
    return hasher.hexdigest()

def get_unique_filename(folder, filename):
    name, ext = os.path.splitext(filename)
    counter = 1
    new_name = filename

    while os.path.exists(os.path.join(folder, new_name)):
        new_name = f"{name}_{counter}{ext}"
        counter += 1

    return new_name

def get_file_date(filepath):
    timestamp = os.path.getmtime(filepath)  # ✅ correct
    return datetime.fromtimestamp(timestamp)

def get_category(file):
    ext = os.path.splitext(file)[1].lower()
    for category, extensions in file_types.items():
        if ext in extensions:
            return category
    return "Others"

def organize():
    all_files = []

    # 🔥 Collect all files first
    for root, dirs, files in os.walk(BASE_FOLDER):
        for file in files:
            full_path = os.path.join(root, file)

            # ❌ Skip files already in correct structure
            if "Duplicates" in full_path:
                continue

            all_files.append(full_path)

    # 🔥 Process files
    for file_path in all_files:
        try:
            file = os.path.basename(file_path)

            file_hash = get_file_hash(file_path)

            # 🔁 Duplicate
            if file_hash in hash_map:
                dup_folder = os.path.join(BASE_FOLDER, "Duplicates")
                os.makedirs(dup_folder, exist_ok=True)

                unique_name = get_unique_filename(dup_folder, file)
                shutil.move(file_path, os.path.join(dup_folder, unique_name))

                print(f"Duplicate: {file}")
                continue

            hash_map[file_hash] = file

            category = get_category(file)
            file_date = get_file_date(file_path)

            year = str(file_date.year)
            month = MONTHS[file_date.month]

            final_folder = os.path.join(BASE_FOLDER, category, year, month)
            os.makedirs(final_folder, exist_ok=True)

            unique_name = get_unique_filename(final_folder, file)
            destination = os.path.join(final_folder, unique_name)

            # ❗ Avoid moving if already in correct place
            if os.path.abspath(file_path) == os.path.abspath(destination):
                continue

            shutil.move(file_path, destination)

            print(f"Moved: {file} → {category}/{year}/{month}")

        except Exception as e:
            print(f"Error: {file_path} → {e}")

organize()

print("\n✅ RE-ORGANIZED successfully!")