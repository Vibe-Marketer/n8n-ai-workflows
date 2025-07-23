import os

def find_files(filename_to_find, output_file):
    with open(output_file, 'w') as f:
        for root, dirs, files in os.walk('.'):
            for file in files:
                if file.endswith(filename_to_find):
                    f.write(os.path.join(root, file) + '\n')

if __name__ == "__main__":
    find_files('.md', 'markdown_files.txt')