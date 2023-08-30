import os
from datetime import datetime

def list_files(startpath, ignore_git, use_icons):
    folder_icon = "\U0001F4C1" if use_icons else "Folder:"
    file_icon = "\U0001F4C4" if use_icons else "File:"
    structure = ""
    
    for root, dirs, files in os.walk(startpath):
        if ignore_git and ".git" in root:
            continue
            
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * level
        
        structure += '{}{} {}\n'.format(indent, folder_icon, os.path.basename(root))
        sub_indent = ' ' * 4 * (level + 1)
        
        for f in files:
            structure += '{}{} {}\n'.format(sub_indent, file_icon, f)
    return structure

def main():
    folder_path = input("Enter the path of the folder (hit Enter for current folder): ")
    if not folder_path:
        folder_path = os.getcwd()
    folder_path = os.getcwd()
    show_in_terminal = input("Display in terminal? (Y/N): ").strip().lower()
    output_txt = input("Output to .txt file? (Y/N): ").strip().lower()
    include_git = input("Include .git files? (Y/N): ").strip().lower()
    use_dashes = input("Use dashes for indentation? (Y/N): ").strip().lower()
    use_icons = input("Use icons for folders and files? (Y/N): ").strip().lower()
    
    ignore_git = include_git != 'y'
    use_icons = use_icons == 'y'
    
    folder_structure = list_files(folder_path, ignore_git, use_icons)
    
    if output_txt == 'y':
        txt_filename = "{}_folder_structure.txt".format(os.path.basename(folder_path))
        
        if os.path.exists(txt_filename):
            overwrite = input(f"{txt_filename} already exists. Overwrite? (Y/N): ").strip().lower()
            if overwrite != 'y':
                timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
                txt_filename = f"{os.path.basename(folder_path)}_folder_structure_{timestamp}.txt"
        
        with open(txt_filename, "w") as f:
            if use_dashes == 'y':
                f.write(folder_structure.replace(" ", "-"))
            else:
                f.write(folder_structure)
    
    if show_in_terminal == 'y':
        print(folder_structure)

if __name__ == "__main__":
    main()
