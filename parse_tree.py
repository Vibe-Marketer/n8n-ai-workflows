import os

def find_readme_files(tree_file):
    readme_files = []
    with open(tree_file, 'r') as f:
        for line in f:
            if 'README.md' in line:
                # Extract the path from the line
                path = line.split(' ')[-1].strip()
                readme_files.append(path)
    return readme_files

if __name__ == '__main__':
    readme_files = find_readme_files('file_tree.txt')
    for readme in readme_files:
        print(readme)