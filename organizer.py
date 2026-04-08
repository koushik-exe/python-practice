import os
import shutil
import hashlib
from datetime import datetime

source_folder = r"C:\Users\ckous\Desktop\Jose Catherine"

file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".webp"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Audio": [".mp3", ".wav", ".opus"],
    "Documents": [".pdf", ".txt", ".docx"],
    "Spreadsheets": [".xlsx", ".csv"],
    "Presentations": [".pptx", ".ppt"],
    "Contacts": [".vcf"],
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

def organize_files(folder):
    for root, dirs, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(root, file)

            if not os.path.exists(file_path):
                continue

            _, ext = os.path.splitext(file)
            ext = ext.lower()

            # 📱 WhatsApp detection
            if "whatsapp" in file.lower():
                base_folder = "WhatsApp"
            else:
                base_folder = "General"

            # 🖼️ Screenshot detection
            if "screenshot" in file.lower():
                category = "Screenshots"
            else:
                category = "Others"

                for cat, extensions in file_types.items():
                    if ext in extensions:
                        category = cat
                        break

            final_folder = os.path.join(folder, base_folder, category)
            os.makedirs(final_folder, exist_ok=True)

            # 🔍 Duplicate detection
            file_hash = get_file_hash(file_path)

            if file_hash in hash_map:
                dup_folder = os.path.join(folder, "Duplicates")
                os.makedirs(dup_folder, exist_ok=True)

                unique_name = get_unique_filename(dup_folder, file)
                shutil.move(file_path, os.path.join(dup_folder, unique_name))
                print(f"Duplicate: {file}")
            else:
                hash_map[file_hash] = file

                unique_name = get_unique_filename(final_folder, file)
                shutil.move(file_path, os.path.join(final_folder, unique_name))
                print(f"Moved: {file} → {category}")

# Run
organize_files(source_folder)

print("\n✅ Clean organization completed!")