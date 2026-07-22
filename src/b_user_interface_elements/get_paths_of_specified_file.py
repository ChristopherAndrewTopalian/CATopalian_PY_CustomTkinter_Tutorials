import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(ROOT_DIR, "webp_manifest.md")
TARGET_FILENAME = "001.webp"
PATH_PREFIX = "src/b_user_interface_elements/"  # <-- new: whatever should go in front of every path


def format_name(folder_name):
    return folder_name.replace("_", " ").title()


def main():
    lines = []

    for current_dir, dirs, files in os.walk(ROOT_DIR):
        for file in files:
            if file.lower() == TARGET_FILENAME:
                full_path = os.path.join(current_dir, file)
                rel_path = os.path.relpath(full_path, ROOT_DIR)
                rel_path = rel_path.replace("\\", "/")

                full_rel_path = f"{PATH_PREFIX}/{rel_path}"

                folder_name = os.path.basename(current_dir)
                display_name = format_name(folder_name)

                lines.append(f"![{display_name}]({full_rel_path})")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"Found {len(lines)} matching files. Written to {OUTPUT_FILE}")
    input("Press Enter to close...")


if __name__ == "__main__":
    main()

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

