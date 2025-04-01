''' Source for various Linked List implementations.
'''


class ListNode:
    """ A simple singly linked list node
    """
    def __init__(self, val):
        self.val = val
        self.next = None
    
    def __str__(self):
        return str(self.val)
    