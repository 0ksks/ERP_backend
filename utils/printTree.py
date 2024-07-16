import os


def print_tree(startPath, prefix=""):
    items: list = os.listdir(startPath)
    items.sort(key=lambda x: x[0].lower())

    # Ensure __init__.py is first if it exists
    files = [
        item
        for item in items
        if not os.path.isdir(os.path.join(startPath, item)) and item != ".DS_Store"
    ]
    if "__init__.py" in files:
        files.remove("__init__.py")
        files.insert(0, "__init__.py")

    folders = [
        item
        for item in items
        if os.path.isdir(os.path.join(startPath, item))
           and item != ".git"
           and item != "__pycache__"
    ]

    for i, name in enumerate(folders + files):
        path = os.path.join(startPath, name)
        if i == len(folders + files) - 1:
            connector = "└──"
            extension = "    "
        else:
            connector = "├──"
            extension = "│   "
        print(prefix + connector + name)
        if os.path.isdir(path):
            print_tree(path, prefix + extension)


if __name__ == "__main__":
    current_path = os.getcwd()
    print_tree(current_path)
