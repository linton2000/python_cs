""" Contains node definitions for linked lists & trees.
"""
from typing import Optional
import textwrap


class ListNode:
    """ A simple singly linked list node.
    """
    def __init__(self, val):
        self.val = val
        self.next: Optional[ListNode] = None
    
    def __str__(self) -> str:
        return str(self.val)
    

class TreeNode:
    """ A node for a binary tree.
    """
    def __init__(self, val):
        self.val = val
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None

    def __str__(self) -> str:
        return str(self.val)
    
    def __repr__(self) -> str:
        left = self.left.val if self.left else None
        right = self.right.val if self.right else None
        return f'TreeNode: {str(self.val)}\n- Left Child: {str(left)}\n- Right Child: {str(right)}'
    