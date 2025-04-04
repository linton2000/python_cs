""" Contains node definitions for linked lists & trees.
"""


class ListNode:
    """ A simple singly linked list node.
    """
    def __init__(self, val):
        self.val = val
        self.next = None
    
    def __str__(self):
        return str(self.val)
    

class TreeNode:
    """ A node for a binary tree.
    """
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.val)
    