import os
from datetime import datetime

def list_files(startpath, ignore_git, use_icons, tree_view, include_node_modules):
    folder_icon = "\U0001F4C1" if use_icons else "Folder:"
    file_icon = "\U0001F4C4" if use_icons else "File:"
    
    tree_folder = "├── " if tree_view else ""
    tree_file = "│   " if tree_view else ' ' * 4
    
    structure = ""

    for root, dirs, files in os.walk(startpath):
        # Skip entire directories if they are .git or node_modules (if flagged)
        if ignore_git and ".git" in root:
            dirs[:] = []
            continue
        if not include_node_modules and 'node_modules' in root:
            dirs[:] = []
            continue

        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * level if not tree_view else "│   " * level
        structure += '{}{}{} {}\n'.format(indent, tree_folder, folder_icon, os.path.basename(root))
        sub_indent = ' ' * 4 * (level + 1) if not tree_view else "│   " * (level + 1)
        for f in files:
            structure += '{}{}{} {}\n'.format(sub_indent, tree_file, file_icon, f)
            
    return structure

def list_full_paths(startpath, ignore_git, include_node_modules):
    startpath = os.path.abspath(startpath)
    paths = []
    
    # Add the starting directory with a trailing slash
    paths.append(startpath + os.sep)
    
    for root, dirs, files in os.walk(startpath):
        # Skip directories if we want to ignore .git or node_modules
        if ignore_git and ".git" in root:
            dirs[:] = []
            continue
        if not include_node_modules and 'node_modules' in root:
            dirs[:] = []
            continue

        # For each directory (skip the starting folder, already added)
        if root != startpath:
            paths.append(root)
        for file in files:
            paths.append(os.path.join(root, file))
    return "\n".join(paths)

def main():
    folder_path = input("Enter the path of the folder (hit Enter for current folder): ").strip()
    if not folder_path:
        folder_path = os.getcwd()

    # New option: list full paths instead of a tree view
    full_paths_option = input("List full paths? (Y/N): ").strip().lower() == 'y'
    
    if not full_paths_option:
        show_in_terminal = input("Display in terminal? (Y/N): ").strip().lower() == 'y'
        output_txt = input("Output to .txt file? (Y/N): ").strip().lower() == 'y'
        include_git = input("Include .git files? (Y/N): ").strip().lower() == 'y'
        include_node_modules = input("Include node_modules folder? (Y/N): ").strip().lower() == 'y'
        use_dashes = input("Use dashes for indentation? (Y/N): ").strip().lower() == 'y'
        use_icons = input("Use icons for folders and files? (Y/N): ").strip().lower() == 'y'
        tree_view = input("Use tree-like structure? (Y/N): ").strip().lower() == 'y'
    
        ignore_git = not include_git
        folder_structure = list_files(folder_path, ignore_git, use_icons, tree_view, include_node_modules)
    
        if output_txt:
            txt_filename = "{}_folder_structure.txt".format(os.path.basename(folder_path))
            if os.path.exists(txt_filename):
                overwrite = input(f"{txt_filename} already exists. Overwrite? (Y/N): ").strip().lower()
                if overwrite != 'y':
                    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
                    txt_filename = f"{os.path.basename(folder_path)}_folder_structure_{timestamp}.txt"
            with open(txt_filename, "w") as f:
                if use_dashes:
                    f.write(folder_structure.replace(" ", "-"))
                else:
                    f.write(folder_structure)
    
        if show_in_terminal:
            print(folder_structure)
    
    else:
        # For full paths mode, we still want to check for .git and node_modules
        include_git = input("Include .git files? (Y/N): ").strip().lower() == 'y'
        include_node_modules = input("Include node_modules folder? (Y/N): ").strip().lower() == 'y'
        ignore_git = not include_git

        full_paths = list_full_paths(folder_path, ignore_git, include_node_modules)
        show_in_terminal = input("Display in terminal? (Y/N): ").strip().lower() == 'y'
        output_txt = input("Output to .txt file? (Y/N): ").strip().lower() == 'y'
    
        if output_txt:
            txt_filename = "{}_full_paths.txt".format(os.path.basename(folder_path))
            if os.path.exists(txt_filename):
                overwrite = input(f"{txt_filename} already exists. Overwrite? (Y/N): ").strip().lower()
                if overwrite != 'y':
                    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
                    txt_filename = f"{os.path.basename(folder_path)}_full_paths_{timestamp}.txt"
            with open(txt_filename, "w") as f:
                f.write(full_paths)
    
        if show_in_terminal:
            print(full_paths)

if __name__ == "__main__":
    main()