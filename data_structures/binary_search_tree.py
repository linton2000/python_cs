from abc import abstractmethod
from typing import Optional, Union
from node import TreeNode


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
    def __str__(self) -> str:
        """ Returns a string representation of the BST.
        """
        pass


class LinkedListBST(BinarySearchTree):
    """ A linked list-based implementation of a Binary Search Tree.
    Assumes there are no duplicate node values.
    """
    
    def __init__(self):
        super().__init__()
        self.root: Optional[TreeNode] = None
    
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
        pass

    def __str__(self) -> None:
        pass


if __name__ == '__main__':
    bst = LinkedListBST()
    bst.insert(1)
    bst.insert(4)
    bst.insert(8)
    print(bst.search(4))
