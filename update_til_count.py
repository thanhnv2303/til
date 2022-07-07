"""
count_tils.py
Updates the number of TIL files (All Markdown
files except the README.md) in the README
and adds it to the staging area.
"""

import os
import re
import subprocess


def get_readme_contents() -> str:
    with open("README.md", "r", encoding="utf-8") as readme:
        return readme.read()


def get_til_counts() -> int:
    count = 0
    for _, _, files in os.walk("."):
        for file in files:
            if file.endswith(".md") and file != "README.md":
                count += 1
    return count


def update_readme_count(old_readme_contents: str, til_count: int) -> None:
    new_readme_contents = re.sub(
        r"_\d+ TILs and counting..._",
        f"_{til_count} TILs and counting..._",
        old_readme_contents,
    )

    with open("README.md", "w", encoding="utf-8") as readme:
        readme.write(new_readme_contents)


if __name__ == "__main__":
    try:
        old_readme_contents = get_readme_contents()

        til_count = get_til_counts()

        update_readme_count(old_readme_contents, til_count)

        print(f"Updated the TIL count in the README.md to {til_count}")

        # Add the modified README file to the staging area for it to be committed
        subprocess.run(["git", "add", "README.md"])

        print("README.md staged for commit")
    except Exception as e:
        print("Error:", e)
