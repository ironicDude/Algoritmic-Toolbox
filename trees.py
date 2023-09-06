class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def list_to_binary_tree(lst):
    if not lst:
        return None

    # Create the root node with the first element of the list
    root = Node(lst[0])

    # Iterate over the remaining elements in the list
    for value in lst[1:]:
        # Call a helper function to insert the value into the binary tree
        insert_into_tree(root, value)

    return root

def insert_into_tree(root, value):
    if value < root.value:
        if root.left is None:
            root.left = Node(value)
        else:
            insert_into_tree(root.left, value)
    else:
        if root.right is None:
            root.right = Node(value)
        else:
            insert_into_tree(root.right, value)

def preorder_traversal(root):
    if root is None:
        return

    # Print the value of the current node
    print(root.value)

    # Traverse the left subtree
    preorder_traversal(root.left)

    # Traverse the right subtree
    preorder_traversal(root.right)



def in_order_traversal(root):
    if root is None:
        return

    # Recursively traverse the left subtree
    in_order_traversal(root.left)

    # Visit the current node (print or process its value)
    print(root.value)

    # Recursively traverse the right subtree
    in_order_traversal(root.right)

def post_order_traversal(root):
    if root is None:
        return

    # Recursively traverse the left subtree
    post_order_traversal(root.left)

    # Recursively traverse the right subtree
    post_order_traversal(root.right)

    # Visit the current node (print or process its value)
    print(root.value)

def count_inner_and_leaf_nodes(root):
    if root is None:
        return 0, 0

    # If the current node is a leaf node
    if root.left is None and root.right is None:
        return 0, 1

    # Recursively count the inner and leaf nodes in the left and right subtrees
    left_inner, left_leaf = count_inner_and_leaf_nodes(root.left)
    right_inner, right_leaf = count_inner_and_leaf_nodes(root.right)

    # Calculate the total inner and leaf nodes
    inner_nodes = left_inner + right_inner + 1
    leaf_nodes = left_leaf + right_leaf

    return inner_nodes, leaf_nodes

def sketch_binary_tree(root, prefix='', is_left=True):
    if root is None:
        return

    # Create a marker for the current node's position
    marker = '|-- ' if is_left else '`-- '

    # Print the value of the current node
    print(prefix + marker + str(root.value))

    # Calculate the new prefix for child nodes
    new_prefix = prefix + '|   ' if is_left else prefix + '    '

    # Recursively sketch the left and right subtrees
    sketch_binary_tree(root.left, new_prefix, True)
    sketch_binary_tree(root.right, new_prefix, False)

def is_balanced(root):
    if root is None:
        return True

    # Get the height of the left subtree
    left_height = get_height(root.left)

    # Get the height of the right subtree
    right_height = get_height(root.right)

    # Check if the difference in heights is greater than 1
    if abs(left_height - right_height) > 1:
        return False

    # Recursively check if both subtrees are balanced
    return is_balanced(root.left) and is_balanced(root.right)


def get_height(node):
    if node is None:
        return 0

    # Recursively calculate the height of the subtree
    left_height = get_height(node.left)
    right_height = get_height(node.right)

    # Return the maximum height plus 1 for the current node
    return max(left_height, right_height) + 1

def is_linear(root):
    if root is None:
        return True

    # If the current node has both left and right children, it is not linear
    if root.left is not None and root.right is not None:
        return False

    # Recursively check if the left and right subtrees are linear
    return is_linear(root.left) and is_linear(root.right)


tree = list_to_binary_tree([23,13,61,12,18,59,235,1,62,135])
sketch_binary_tree(tree)
# preorder_traversal(tree)
print('\n')
# in_order_traversal(tree)
post_order_traversal(tree)
print(is_balanced(tree))



