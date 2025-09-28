from tree.avl import insert as insertavl
from tree.bst import insert as insertbst

def sum_tree(node):
    if node is None:
        return 0
    
    if hasattr(node, 'val'):     #bst
        value = node.val
    elif hasattr(node, 'key'):   #avl
        value = node.key
    else:
        raise AttributeError("Node has no 'val' nor 'key'")
    
    return value + sum_tree(node.left) + sum_tree(node.right)




tree_vals = [20, 10, 30, 5, 15]


root_bst = None
root_avl = None

for key in tree_vals:
    root_bst = insertbst(root_bst, key)
    root_avl = insertavl(root_avl, key)

print("Min value in BST:", sum_tree(root_bst))
print("Min value in AVL:", sum_tree(root_avl))