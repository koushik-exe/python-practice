import os
import shutil
import hashlib
import time
from datetime import datetime

# ============================================================
#   🔥 GOD MODE ORGANIZER
#   Phase 1 → Organize Everything (Files + Duplicates perfectly)
#   Phase 2 → Deep Verification (Auto runs after Phase 1)
# ============================================================

# 📂 Paths
SOURCE_FOLDER = r"C:\Users\ckous\Desktop\Pravetha"
DEST_FOLDER   = r"C:\Users\ckous\Desktop\Pravetha Organizer"
LOG_FILE      = os.path.join(DEST_FOLDER, "god_mode_log.txt")
REPORT_FILE   = os.path.join(DEST_FOLDER, "deep_verification.txt")

# 📁 Categories
file_types = {
    "Images":     [".jpg",".jpeg",".png",".webp",".bmp",".gif",".tiff",".tif",".heic",".heif",".svg"],
    "RAW_Images": [".raw",".cr2",".nef",".arw",".dng"],
    "Videos":     [".mp4",".mkv",".avi",".mov",".wmv",".flv",".webm",".mpeg",".mpg",".3gp",".m4v",".ts",".vob"],
    "Audio":      [".mp3",".wav",".aac",".flac",".ogg",".opus",".m4a",".wma",".aiff",".alac"],
    "Documents":  [".pdf",".txt",".doc",".docx",".odt",".xls",".xlsx",".ods",".ppt",".pptx",".odp",".csv",".rtf",".md",".epub"],
    "Archives":   [".zip",".rar",".7z",".tar",".gz",".bz2",".xz",".iso"],
    "Code":       [".py",".js",".html",".css",".java",".c",".cpp",".json",".xml",".yml",".yaml",".sh",".bat"]
}

MONTHS = {
    1:"January", 2:"February", 3:"March",    4:"April",
    5:"May",     6:"June",     7:"July",      8:"August",
    9:"September",10:"October",11:"November",12:"December"
}

hash_map = {}

# ============================================================
# 🔐 SHA-256 Hash
# ============================================================
def get_file_hash(filepath):
    hasher = hashlib.sha256()
    with open(filepath, 'rb') as f:
        while chunk := f.read(8192):
            hasher.update(chunk)
    return hasher.hexdigest()

# ============================================================
# 🛡️ Safe unique filename
# ============================================================
def get_unique_filename(folder, filename):
    name, ext = os.path.splitext(filename)
    counter = 1
    new_name = filename
    while os.path.exists(os.path.join(folder, new_name)):
        new_name = f"{name}_{counter}{ext}"
        counter += 1
    return new_name

# ============================================================
# 📸 EXIF Date (for images)
# ============================================================
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

# ============================================================
# 📅 Best date for file
# ============================================================
def get_file_date(filepath):
    ext = os.path.splitext(filepath)[1].lower()
    if ext in file_types["Images"] or ext in file_types["RAW_Images"]:
        exif_date = get_image_date(filepath)
        if exif_date:
            return exif_date
    return datetime.fromtimestamp(os.path.getmtime(filepath))

# ============================================================
# 📁 Get category
# ============================================================
def get_category(file):
    ext = os.path.splitext(file)[1].lower()
    for category, exts in file_types.items():
        if ext in exts:
            return category
    return "Others"

# ============================================================
# 📝 Log with timestamp
# ============================================================
def log(msg):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    full_msg = f"[{timestamp}] {msg}"
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(full_msg + "\n")

# ============================================================
# 📊 Folder size calculator
# ============================================================
def get_folder_size(folder):
    total = 0
    if not os.path.exists(folder):
        return 0
    for root, dirs, files in os.walk(folder):
        for file in files:
            try:
                total += os.path.getsize(os.path.join(root, file))
            except:
                pass
    return total

def format_size(size_bytes):
    if size_bytes == 0:
        return "0 Bytes"
    elif size_bytes < 1024:
        return f"{size_bytes} Bytes"
    elif size_bytes < 1024 ** 2:
        return f"{size_bytes/1024:.2f} KB"
    elif size_bytes < 1024 ** 3:
        return f"{size_bytes/(1024**2):.2f} MB"
    else:
        return f"{size_bytes/(1024**3):.2f} GB"

# ============================================================
# 🔥 STEP 1: Scan existing Organizer files
# ============================================================
def scan_existing_files():
    print("🔍 Scanning Organizer for existing files...")
    for root, dirs, files in os.walk(DEST_FOLDER):
        for file in files:
            file_path = os.path.join(root, file)
            if file_path in [LOG_FILE, REPORT_FILE]:
                continue
            try:
                file_hash = get_file_hash(file_path)
                hash_map[file_hash] = file_path
            except:
                pass
    print(f"✅ Loaded {len(hash_map)} existing files into memory\n")

# ============================================================
# 🚀 PHASE 1: Organize + Fix Duplicates Together (GOD MODE)
# ============================================================
def phase1_organize():
    print("=" * 55)
    print("   🚀 PHASE 1 — Organizing Files (GOD MODE)")
    print("=" * 55)

    moved = 0
    duplicates = 0
    errors = 0

    scan_existing_files()

    for root, dirs, files in os.walk(SOURCE_FOLDER):
        for file in files:
            file_path = os.path.join(root, file)

            try:
                file_hash   = get_file_hash(file_path)
                category    = get_category(file)
                date        = get_file_date(file_path)
                year        = str(date.year)
                month       = MONTHS[date.month]

                normal_folder    = os.path.join(DEST_FOLDER, category, year, month)

                # ✅ GOD MODE FIX: Duplicates organized perfectly (Category/Year/Month)
                duplicate_folder = os.path.join(DEST_FOLDER, "Duplicates", category, year, month)

                if file_hash in hash_map:
                    # 🔁 It's a duplicate — move to properly organized Duplicates folder
                    os.makedirs(duplicate_folder, exist_ok=True)
                    unique_name = get_unique_filename(duplicate_folder, file)
                    dest_path   = os.path.join(duplicate_folder, unique_name)
                    shutil.move(file_path, dest_path)

                    msg = f"🔁 DUPLICATE  | {file} → Duplicates/{category}/{year}/{month}/{unique_name}"
                    print(msg)
                    log(msg)
                    duplicates += 1
                    continue

                # ✅ New unique file
                hash_map[file_hash] = file_path
                os.makedirs(normal_folder, exist_ok=True)
                unique_name = get_unique_filename(normal_folder, file)
                dest_path   = os.path.join(normal_folder, unique_name)
                shutil.move(file_path, dest_path)

                msg = f"✅ MOVED      | {file} → {category}/{year}/{month}/{unique_name}"
                print(msg)
                log(msg)
                moved += 1

            except Exception as e:
                msg = f"🚨 ERROR      | {file} → {e}"
                print(msg)
                log(msg)
                errors += 1

    print()
    print(f"   ✅ Files Moved    : {moved}")
    print(f"   🔁 Duplicates     : {duplicates}")
    print(f"   🚨 Errors         : {errors}")
    print()

    return moved, duplicates, errors

# ============================================================
# 🔍 PHASE 2: Deep Verification (Auto runs after Phase 1)
# ============================================================
def phase2_verify():
    print("=" * 55)
    print("   🔍 PHASE 2 — Deep Verification")
    print("=" * 55)

    # Build normal files index
    normal_index = {}
    print("   Building normal files index...")

    for root, dirs, files in os.walk(DEST_FOLDER):
        if "duplicates" in root.lower():
            continue

        for file in files:
            file_path = os.path.join(root, file)
            if file_path in [LOG_FILE, REPORT_FILE]:
                continue

            try:
                file_hash = get_file_hash(file_path)
                parts     = root.split(os.sep)

                if len(parts) >= 3:
                    category = parts[-3]
                    year     = parts[-2]
                    month    = parts[-1]
                    key      = (category, year, month)

                    if key not in normal_index:
                        normal_index[key] = {}
                    normal_index[key][file_hash] = file_path
            except:
                pass

    # Now verify duplicates
    perfect = []
    wrong   = []
    missing = []

    print("   Verifying duplicates...\n")

    for root, dirs, files in os.walk(DEST_FOLDER):
        if "duplicates" not in root.lower():
            continue

        for file in files:
            file_path = os.path.join(root, file)

            try:
                file_hash = get_file_hash(file_path)
                parts     = root.split(os.sep)

                if len(parts) >= 3:
                    category = parts[-3]
                    year     = parts[-2]
                    month    = parts[-1]
                    key      = (category, year, month)

                    if key in normal_index and file_hash in normal_index[key]:
                        perfect.append(file_path)
                    else:
                        found_elsewhere = any(
                            file_hash in normal_index[k] for k in normal_index
                        )
                        if found_elsewhere:
                            wrong.append(file_path)
                        else:
                            missing.append(file_path)
            except:
                missing.append(file_path)

    # Save report
    with open(REPORT_FILE, "w", encoding="utf-8") as f:
        f.write("🔥 GOD MODE — DEEP VERIFICATION REPORT\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 60 + "\n\n")

        f.write(f"✅ PERFECT MATCH ({len(perfect)} files):\n\n")
        for fp in perfect:
            f.write(fp + "\n")

        f.write("\n" + "=" * 60 + "\n")
        f.write(f"\n⚠️ WRONG LOCATION ({len(wrong)} files):\n\n")
        for fp in wrong:
            f.write(fp + "\n")

        f.write("\n" + "=" * 60 + "\n")
        f.write(f"\n🚨 MISSING — CRITICAL ({len(missing)} files):\n\n")
        for fp in missing:
            f.write(fp + "\n")

    print(f"   ✅ Verified Perfect : {len(perfect)}")
    print(f"   ⚠️  Wrong Location  : {len(wrong)}")
    print(f"   🚨 Missing (Critical): {len(missing)}")
    print()

    return perfect, wrong, missing

# ============================================================
# ▶ MAIN — GOD MODE RUN
# ============================================================
def god_mode():

    # 🛡️ Safety Check
    if not os.path.exists(SOURCE_FOLDER):
        print(f"🚨 ERROR: Source folder not found!\n   {SOURCE_FOLDER}")
        return

    source_files = sum(len(files) for _, _, files in os.walk(SOURCE_FOLDER))
    if source_files == 0:
        print("⚠️  WARNING: Messy folder is already EMPTY! Nothing to organize.")
        return

    os.makedirs(DEST_FOLDER, exist_ok=True)

    print()
    print("=" * 55)
    print("        🔥 GOD MODE ORGANIZER — START")
    print("=" * 55)

    # 📊 Before sizes
    before_messy     = get_folder_size(SOURCE_FOLDER)
    before_organizer = get_folder_size(DEST_FOLDER)

    print()
    print("📊 BEFORE:")
    print(f"   Messy Folder   : {format_size(before_messy)}")
    print(f"   Organizer      : {format_size(before_organizer)}")
    print(f"   Total Files    : {source_files} files waiting")
    print()

    # ⏱️ Start timer
    start_time = time.time()

    # 🚀 Phase 1
    moved, duplicates, errors = phase1_organize()

    # 🔍 Phase 2
    perfect, wrong, missing = phase2_verify()

    # ⏱️ Stop timer
    elapsed     = time.time() - start_time
    minutes     = int(elapsed // 60)
    seconds     = int(elapsed % 60)
    time_str    = f"{minutes} min {seconds} sec" if minutes > 0 else f"{seconds} seconds"

    # 📊 After sizes
    after_messy     = get_folder_size(SOURCE_FOLDER)
    after_organizer = get_folder_size(DEST_FOLDER)

    # ============================================================
    # 🖥️ FINAL TERMINAL REPORT
    # ============================================================
    print("=" * 55)
    print("        🔥 GOD MODE — FINAL RESULTS")
    print("=" * 55)
    print()
    print("📊 BEFORE vs AFTER:")
    print(f"   Messy Folder   : {format_size(before_messy)}  →  {format_size(after_messy)}")
    print(f"   Organizer      : {format_size(before_organizer)}  →  {format_size(after_organizer)}")
    print()
    print("📁 PHASE 1 — Organize Results:")
    print(f"   ✅ Files Moved     : {moved}")
    print(f"   🔁 Duplicates      : {duplicates}")
    print(f"   🚨 Errors          : {errors}")
    print()
    print("🔍 PHASE 2 — Verification Results:")
    print(f"   ✅ Verified Perfect : {len(perfect)}")
    print(f"   ⚠️  Wrong Location  : {len(wrong)}")
    print(f"   🚨 Missing (Critical): {len(missing)}")
    print()

    # ⚠️ Loud warnings if problems found
    if len(wrong) > 0:
        print("=" * 55)
        print(f"  ⚠️  WARNING: {len(wrong)} files are in WRONG LOCATION!")
        print(f"     Check: {REPORT_FILE}")
        print("=" * 55)

    if len(missing) > 0:
        print("=" * 55)
        print(f"  🚨 CRITICAL: {len(missing)} files are MISSING!")
        print(f"     Check: {REPORT_FILE}")
        print("=" * 55)

    if len(wrong) == 0 and len(missing) == 0:
        print("  🎉 PERFECT! Everything organized and verified!")

    print()
    print(f"⏱️  Time Taken      : {time_str}")
    print(f"📝 Log File        : {LOG_FILE}")
    print(f"📋 Report File     : {REPORT_FILE}")
    print()
    print("=" * 55)
    print("        ✅ GOD MODE COMPLETE!")
    print("=" * 55)
    print()

    # Log summary
    log(f"{'='*50}")
    log(f"GOD MODE COMPLETE | Moved:{moved} | Duplicates:{duplicates} | Errors:{errors} | Perfect:{len(perfect)} | Wrong:{len(wrong)} | Missing:{len(missing)} | Time:{time_str}")
    log(f"{'='*50}")

# ▶ RUN
god_mode()
