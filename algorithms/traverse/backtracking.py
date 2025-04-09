from data_structures.node import TreeNode


def backtrack(root: TreeNode, path: list[TreeNode]) -> bool:
    """ A standard backtracking algorithm implementation for a binary tree.
    Uses DFS to traverse down the tree until it hits a 0 value node or a leaf node.
    If leaf node is found, returns True and `path` variable has a valid path from root to leaf.
    If a 0 value node is found, backtracks up to recursively find another valid path.
    If no valid paths are found, this function returns False with an empty `path` list.
    """
    if not root or root.val == 0:
        return False  # Need to backtrack up
    
    path.append(root)  # Assumed as valid path for now
    if not root.left and not root.right:
        return True  # Reached a leaf node, yay!
    if backtrack(root.left, path):  # Traverse down left subtree
        return True
    if backtrack(root.right, path):  # Traverse down right subtree
        return True
    
    path.pop()  # No valid path under both left & right subtrees of root. So removing root
    return False

def build_tree() -> TreeNode:
    r""" Generates a binary tree as input into the backtracking algorithm.
    Places 0 value nodes at random places in the tree. Allows at least one
    correct path from root to leaf node for backtracking success.

    Result Tree:
          4
         / \
        0   1
       /   / \
      7   2   8
         /
        0    
    """
    n1 = TreeNode(4)
    n1.left = TreeNode(0)
    n1.right = TreeNode(1)
    n1.left.left = TreeNode(7)
    n1.right.left = TreeNode(2)
    n1.right.right = TreeNode(8)
    n1.right.left.left = TreeNode(0)

    return n1


if __name__ == '__main__':
    path: list[TreeNode] = []
    backtrack(build_tree(), path)
    print(path)
