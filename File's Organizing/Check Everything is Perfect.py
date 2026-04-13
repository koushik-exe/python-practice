import os
import hashlib

BASE_FOLDER = r"C:\Users\ckous\Desktop\Organizer"
REPORT_FILE = os.path.join(BASE_FOLDER, "deep_verification.txt")

# 🔐 SHA-256
def get_file_hash(filepath):
    hasher = hashlib.sha256()
    with open(filepath, 'rb') as f:
        while chunk := f.read(8192):
            hasher.update(chunk)
    return hasher.hexdigest()

# 🔍 Scan NORMAL files into structured map
def build_normal_index():
    index = {}

    print("🔍 Indexing normal files...")

    for root, dirs, files in os.walk(BASE_FOLDER):
        if "duplicates" in root.lower():
            continue

        for file in files:
            file_path = os.path.join(root, file)

            try:
                file_hash = get_file_hash(file_path)

                # Extract Category/Year/Month
                parts = root.split(os.sep)

                if len(parts) >= 4:
                    category = parts[-3]
                    year = parts[-2]
                    month = parts[-1]

                    key = (category, year, month)

                    if key not in index:
                        index[key] = {}

                    index[key][file_hash] = file_path

            except:
                pass

    print("✅ Normal index ready")
    return index

# 🔍 Verify duplicates deeply
def verify_duplicates(index):
    perfect = []
    wrong = []
    missing = []

    print("🧾 Verifying duplicates deeply...")

    for root, dirs, files in os.walk(BASE_FOLDER):
        if "duplicates" not in root.lower():
            continue

        for file in files:
            file_path = os.path.join(root, file)

            try:
                file_hash = get_file_hash(file_path)

                parts = root.split(os.sep)

                if len(parts) >= 5:
                    category = parts[-3]
                    year = parts[-2]
                    month = parts[-1]

                    key = (category, year, month)

                    # ✅ Check exact location
                    if key in index and file_hash in index[key]:
                        perfect.append(file_path)

                    else:
                        # 🔍 Check anywhere else
                        found_elsewhere = False

                        for k in index:
                            if file_hash in index[k]:
                                found_elsewhere = True
                                break

                        if found_elsewhere:
                            wrong.append(file_path)
                        else:
                            missing.append(file_path)

            except:
                missing.append(file_path)

    return perfect, wrong, missing

# 🧾 Report
def generate_report(perfect, wrong, missing):
    with open(REPORT_FILE, "w", encoding="utf-8") as f:

        f.write("✅ PERFECT MATCH (SAFE):\n\n")
        for file in perfect:
            f.write(file + "\n")

        f.write("\n" + "="*60 + "\n")

        f.write("\n⚠️ WRONG LOCATION (FOUND ELSEWHERE):\n\n")
        for file in wrong:
            f.write(file + "\n")

        f.write("\n" + "="*60 + "\n")

        f.write("\n🚨 MISSING (CRITICAL ERROR):\n\n")
        for file in missing:
            f.write(file + "\n")

    print(f"✅ Report saved: {REPORT_FILE}")
    print(f"Perfect: {len(perfect)} | Wrong: {len(wrong)} | Missing: {len(missing)}")

# ▶ Run
index = build_normal_index()
perfect, wrong, missing = verify_duplicates(index)
generate_report(perfect, wrong, missing)

print("\n✅ DONE! Deep verification complete.")