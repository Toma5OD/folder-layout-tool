# Folder Layout Tool 📁

## Overview

This project includes Python scripts to visualize the folder structure in a readable way. The main tool is `folder_structure_tool.py`, which offers a variety of features including the option to include `.git` files, output to `.txt` files, and use icons for better visualization.

## Folder Structure
```
📁-folder-layout-tool
----📄-list_folder_structure.py
----📄-list_folder_structure_no_git.py
----📄-folder_structure_tool.py
----📄-README.md
```


## Requirements

- Python 3.x

## Usage

1. Clone this repository or download the script.
    ```bash
    git clone https://github.com/Toma5OD/folder-layout-tool
    ```
2. Open a terminal and navigate to the directory where the script is located.
    ```bash
    cd folder-layout-tool
    ```
3. Run the **main script** `folder_structure_tool.py`:
    ```bash
    python folder_structure_tool.py
    ```

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
$ Enter the path of the folder: /home/USER_NAME/dev/onboarding-os-ci
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
2. **Include .git files? (Y/N)**: Choose whether to include `.git` files in the structure.
3. **Output to .txt file? (Y/N)**: Choose to save the folder structure in a `.txt` file.
4. **Use dashes for indentation? (Y/N)**: Opt for enhanced `.txt` format with dashes instead of spaces.
5. **Display in terminal? (Y/N)**: Display the folder structure in the terminal window.
6. **Use icons for folders and files? (Y/N)**: Icons will be used to indicate folders and files.

## Contributing

Feel free to open an issue or pull request if you find any bugs or have suggestions for improvements.

