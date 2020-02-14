from DataStructures.tree.tree_class import Tree


# prepare tree
tree = Tree()
node_list = [314, 6, 6, 271, 561, 2, 271, 28, 0, 'NaN', 3, 'NaN', 1, 'NaN', 28, 'NaN','NaN','NaN','NaN',17, 'NaN', 401, 257, 'NaN','NaN','NaN','NaN','NaN',641]
node_list = ['A','B','I','C','F','J','O','D','E','NaN','G','NaN','K','NaN','P','NaN','NaN','NaN','NaN','H','NaN','L','N','NaN','NaN','NaN','NaN','NaN','M']
node_list = ['A','B','K','C','H','L','O','D','G','I','J','M','N','NaN','NaN','E','F']
node_list = [1,2,3,4,'NaN','NaN','NaN','NaN',5]
root = tree.generate_tree_from_list(node_list)


# Traversal

# 1. inorder
def inorder_traversal(root):
    if root is None:
        return
    inorder_traversal(root.left)
    print(' {}'.format(root.val), end='')
    inorder_traversal(root.right)


# 2. preorder
def preorder_traversal(root):
    if root is None:
        return
    print(' {}'.format(root.val), end='')
    preorder_traversal(root.left)
    preorder_traversal(root.right)


# 3. postorder
def postorder_traversal(root):
    if root is None:
        return
    postorder_traversal(root.left)
    postorder_traversal(root.right)
    print(' {}'.format(root.val), end='')


# 4. Height of a Tree
def height_of_tree(root):
    if root is None:
        return 0
    return 1 + max(height_of_tree(root.left), height_of_tree(root.right))


# 5. if the tree is height-balanced
def is_height_balanced(root):
    if root is None:
        return True
    if abs(height_of_tree(root.left) - height_of_tree(root.right)) > 1:
        return False
    else:
        return is_height_balanced(root.left) and is_height_balanced(root.right)


def main():
    print('test')
    # inorder_traversal(root)

    # preorder_traversal(root)

    # postorder_traversal(root)

    # h = height_of_tree(root)
    # print(h)

    is_h_b = is_height_balanced(root)
    print(is_h_b)



if __name__ == '__main__':
    main()
