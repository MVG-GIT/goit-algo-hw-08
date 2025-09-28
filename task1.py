from tree.avl import insert as insertavl
from tree.bst import insert as insertbst

def find_min(node):
    if node is None:
        return None
    
    current = node
    while current.left is not None:
        current = current.left

    if hasattr(current, 'val'):     #bst
        return current.val
    elif hasattr(current, 'key'):   #avl
        return current.key
    else:
        raise AttributeError("Node got no 'val' nor 'key'")




tree_vals = [20, 10, 30, 5, 15]


root_bst = None
root_avl = None

for key in tree_vals:
    root_bst = insertbst(root_bst, key)
    root_avl = insertavl(root_avl, key)

print("Min value in BST:", find_min(root_bst))
print("Min value in AVL:", find_min(root_avl))
