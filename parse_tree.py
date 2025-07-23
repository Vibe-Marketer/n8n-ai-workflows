import re

def find_markdown_files(input_file, output_file):
    with open(input_file, 'r') as f:
        content = f.read()

    # Find all paths ending with .md
    md_files = re.findall(r'\./.*\.md', content)

    with open(output_file, 'w') as f:
        for file in md_files:
            f.write(file + '\n')

if __name__ == "__main__":
    find_markdown_files('file_tree.txt', 'markdown_files.txt')