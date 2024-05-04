
def print_tree(tree, level=0, prefix="Root:"):
    if tree is not None:
        print(" " * (level * 4) + prefix + str(tree.data))
        if tree.left is not None or tree.right is not None:
            print_tree(tree.left, level + 1, "L--")
            print_tree(tree.right, level + 1, "R--")

print_tree(new_tree)