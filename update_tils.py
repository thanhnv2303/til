"""
count_tils.py
Updates the number of TIL files (All Markdown
files except the README.md) in the README
"""

import os
import re


def get_readme_contents():
    with open("README.md", "r", encoding="utf-8") as readme:
        return readme.read()


def get_til_counts():
    count = 0
    for _, _, files in os.walk("."):
        for file in files:
            if file.endswith(".md") and file != "README.md":
                count += 1
    return count


def write_readme_contents(contents):
    with open("README.md", "w", encoding="utf-8") as readme:
        readme.write(contents)


if __name__ == "__main__":
    # Get the readme content
    readme_contents = get_readme_contents()

    # Get the number of TIL files
    til_count = get_til_counts()

    # Update the TIL count in the readme content
    readme_contents = re.sub(
        r"_\d+ TILs and counting..._",
        f"_{til_count} TILs and counting..._",
        readme_contents,
    )

    # Write back thee updated content to the readme file
    write_readme_contents(readme_contents)

    print(f"Updated the number of TILs in the README.md to {til_count}")
