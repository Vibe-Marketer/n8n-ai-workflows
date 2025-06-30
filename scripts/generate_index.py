#!/usr/bin/env python3
"""
Generate index.md for workflows
"""
import os
BASE_DIR = "../workflows"
def generate_index():
    for category in os.listdir(BASE_DIR):
        category_path = os.path.join(BASE_DIR, category)
        if os.path.isdir(category_path):
            files = [f for f in os.listdir(category_path) if f.endswith(".json")]
            readme = os.path.join(category_path, "README.md")
            with open(readme, "w") as f:
                f.write(f"# 📂 {category.replace('-', ' ').title()}
\n")
                for wf in files:
                    f.write(f"- `{wf}`\n")
if __name__ == "__main__":
    generate_index()
