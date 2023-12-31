# Folder Layout Tool 📁

## Overview

This project includes Python scripts to visualize the folder structure in a readable way. The main tool is `folder_structure_tool.py`, which offers a variety of features including the option to include `.git` files, output to `.txt` files, and use icons for better visualization and now, the ability to include or exclude the contents of node_modules folders.

![Example of folder structure in terminal](public/image1.png)
*Example of folder structure displayed directly in the terminal.*

## Folder Structure of this Repo

```
📁 folder-layout-tool
    📄 list_folder_structure.py
    📄 list_folder_structure_no_git.py
    📄 folder_structure_tool.py
    📄 README.md
    📄 LICENSE
    📁 public
        📄 image1.png
        📄 image2.png
```

## Requirements

- Python 3.x

## Usage

1. Clone this repository or download the script.
    \```bash
    git clone https://github.com/Toma5OD/folder-layout-tool
    \```
2. Open a terminal and navigate to the directory where the script is located.
    \```bash
    cd folder-layout-tool
    \```
3. Run the **main script** `folder_structure_tool.py`:
    \```bash
    python folder_structure_tool.py
    \```

![Example of `.txt` file output](public/image2.png)
*Example of `.txt` file generated using the tool.*

## Tools Explanation

### `folder_structure_tool.py` (Main Tool)

This is the primary utility in the suite, offering a comprehensive set of features. With this tool, you can:

- Include `.git` files in the output
- Export the folder structure to `.txt` files
- Opt for enhanced text formatting with dashes
- View the folder structure directly in the terminal
- Utilize icons to differentiate between folders and files

#### Example Terminal Interaction

To initiate the tool, execute the following command in your terminal:

```bash
$ python folder_structure_tool.py
```

Upon execution, the terminal will present a series of questions for customization. The sequence of interactions will closely resemble the following:

```bash
$ Enter the path of the folder: /home/USER_NAME/EXAMPLE
$ Display in terminal? (Y/N): 
$ Output to `.txt` file? (Y/N): 
$ Include `.git` files? (Y/N): 
$ Use dashes for indentation? (Y/N): 
$ Use icons for folders and files? (Y/N): 
```

### `list_folder_structure.py`

This tool lists all files and folders, including `.git` directories. It will not create a `.txt` file and will only display the structure in the terminal.

### `list_folder_structure_no_git.py`

This tool lists all files and folders, excluding `.git` directories. It will not create a `.txt` file and will only display the structure in the terminal.

## User Prompts

1. **Enter the path of the folder**: Input the full path of the folder you want to analyze.
2. **Display in terminal? (Y/N)**: Choose whether to display the folder structure in the terminal window.
3. **Output to `.txt` file? (Y/N)**: Decide if you want to save the folder structure in a `.txt` file.
4. **Include `.git` files? (Y/N)**: Specify if `.git` files should be included in the structure.
5. **Use dashes for indentation? (Y/N)**: Opt for an enhanced `.txt` format using dashes instead of spaces for indentation.
6. **Use icons for folders and files? (Y/N)**: Select if icons should be used to indicate folders and files.

## Contributing

Feel free to open an issue or pull request if you find any bugs or have suggestions for improvements.
