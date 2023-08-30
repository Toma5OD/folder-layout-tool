import os

def list_files(startpath, ignore_git=True):
    output = []
    for root, dirs, files in os.walk(startpath):
        if ignore_git and '.git' in root:
            continue
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * level
        output.append(f"{indent}{os.path.basename(root)}/")
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            output.append(f"{subindent}{f}")
    return "\n".join(output)

folder_path = input("Enter the path of the folder: ")
print(list_files(folder_path))
