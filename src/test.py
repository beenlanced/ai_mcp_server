import os
from pathlib import Path

docs_path = Path(__file__).parent.parent / "docs"
print(f"docs_path - {docs_path}")

file_path = (docs_path / "usage.txt").resolve()
print(f"file_path - {file_path}")

print(file_path.is_file())

if file_path.is_file():
    with open(file_path, "r") as file:
        print(file.read())
   
else:
    print("Usage guide not found.")