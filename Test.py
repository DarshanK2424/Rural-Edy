import os


def print_tree(startpath, max_depth=3, exclude_folders=None):
    exclude_folders = set(exclude_folders or [])

    for root, dirs, files in os.walk(startpath):
        # Calculate depth from start path
        depth = root[len(startpath):].count(os.sep)

        if depth > max_depth:
            dirs[:] = []  # Don't go deeper
            continue

        # Remove excluded folders from traversal
        dirs[:] = [d for d in dirs if d not in exclude_folders]

        indent = ' ' * 4 * depth
        print(f"{indent}{os.path.basename(root)}/")

        for f in files:
            print(f"{indent}    {f}")


# Run from project root
print_tree('.', max_depth=3, exclude_folders=['node_modules'])
