from abc import abstractmethod
from typing import Optional, Union, Callable
from enum import Enum, auto
from random import randint
from node import TreeNode


class Order(Enum):
    """ Traversal order options for BFS & DFS traversal
    """
    INORDER = auto()
    PREORDER = auto()
    POSTORDER = auto()


class BinarySearchTree:
    """ Abstract class for various Binary Search Tree ADT implementations.
    """

    def __init__(self):
        self.size = 0

    @abstractmethod
    def search(self, target_val) -> Union[TreeNode, bool]:
        """ Traverse the BST to find and return the target_val node. Returns False
        if target_val node doesn't exist in BST.
        """
        pass

    @abstractmethod
    def insert(self, new_val) -> None:
        """ Sinks the newly inserted node into the right position in the BST.
        Keeps the BST property but does not try to keep a balanced BST.
        """
        pass

    def insert_all(self, vals: list) -> None:
        """ Iteratively runs the insert method on all input array elements.
        """
        for val in vals:
            self.insert(val)

    @abstractmethod
    def remove(self, target_val) -> None:
        """ Finds and removes the target_val node from the BST.
        """
        pass

    @abstractmethod
    def get_min(self, root: TreeNode = None) -> TreeNode:
        """ Finds and returns the node with the minimum value.
        """
        pass

    @abstractmethod
    def get_max(self, root: TreeNode = None) -> TreeNode:
        """ Finds and returns the node with the maximum value.
        """
        pass

    @abstractmethod
    def get_height(self) -> int:
        """ Returns the maximum height of the tree in integers.
        Height defined as no. of nodes from top to bottom, i.e. a BST of 3 nodes has height = 2.
        """
        pass

    @abstractmethod
    def dfs_traversal(self, order: Order, visit: Optional[Callable] = None) -> list:
        """ Performs a depth-first search traversal on all BST nodes according to specified Order.
        Applies the visit() function on each node. Returns a visit-ordered list of node values.
        """
        pass

    @abstractmethod
    def __str__(self) -> str:
        """ Returns a string representation of the BST.
        """
        pass


class LinkedListBST(BinarySearchTree):
    """ A linked list-based implementation of a Binary Search Tree.
    Assumes there are no duplicate node values.
    """
    
    def __init__(self, size: Optional[int] = None):
        super().__init__()
        self.root: Optional[TreeNode] = None
        if size:
            vals = [randint(0, 100) for _ in range(size)]
            self.insert_all(vals)
    
    def search(self, target_val) -> Union[TreeNode, bool]:
        def _recursive_search(root: TreeNode, val) -> Union[TreeNode, bool]:
            if not root:
                return False
            if val > root.val:
                return _recursive_search(root.right, val)
            if val < root.val:
                return _recursive_search(root.left, val)
            if val == root.val:
                return root
        
        return _recursive_search(self.root, target_val)

    def insert(self, new_val) -> None:
        def _recursive_insert(root: TreeNode, val) -> TreeNode:
            if not root:  # Return new node to previous frame in call stack
                return TreeNode(val)
            if val > root.val: # Go down right subtree
                root.right = _recursive_insert(root.right, val)
            elif val < root.val: # Go down left subtree
                root.left = _recursive_insert(root.left, val)
            return root  # Avoids breaking tree structure when root.val == val

        if self.root == None:
            self.root = TreeNode(new_val)
        else:
            _recursive_insert(self.root, new_val)
        self.size += 1
            
    def remove(self, target_val) -> None:
        """ def _recursive_remove(root: Optional[TreeNode]):
            if target_val < root.val:
                _recursive_remove(root.left)
            if target_val > root.val:
                _recursive_remove(root.right)
            if target_val == root.val:
                 """
        pass

    def get_height(self) -> int:
        def _recurse(root: TreeNode):
            if not root:
                return 0  # Empty tree defined as 0
            return 1 + max(_recurse(root.left), _recurse(root.right))
        
        return _recurse(self.root)

    def dfs_traversal(self, order: Order, visit: Optional[Callable] = None) -> list:
        lst = []

        def _visit_append(node: TreeNode):
            if visit:
                visit()
            lst.append(node.val)

        def _recursive_dfs(root: Optional[TreeNode]):
            if not root:
                return
            if order == Order.PREORDER:
                _visit_append(root)
            _recursive_dfs(root.left)
            if order == Order.INORDER:
                _visit_append(root)
            _recursive_dfs(root.right)
            if order == Order.POSTORDER:
                _visit_append(root)
        
        _recursive_dfs(self.root)
        return lst

    def __str__(self) -> None:
        res = ''
        def _pretty_str(node: TreeNode, prefix: str = "", is_left: bool = True) -> str:
            nonlocal res

            if node.right:
                _pretty_str(node.right, prefix + ("│   " if is_left else "    "), False)

            res += prefix + ("└── " if is_left else "┌── ") + str(node.val) + '\n'

            if node.left:
                _pretty_str(node.left, prefix + ("    " if is_left else "│   "), True)

        _pretty_str(self.root)
        return res


if __name__ == '__main__':
    bst = LinkedListBST(10)
    print(bst)
