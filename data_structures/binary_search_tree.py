from abc import abstractmethod
from typing import TypeVar
from linked_list import ListNode

T = TypeVar('T')


class BinarySearchTree:
    """ Abstract class for various Binary Search Tree ADT implementations.
    """

    def __init__(self):
        pass

    @abstractmethod
    def search(self, target):
        pass

    @abstractmethod
    def insert(self, target):
        pass

    @abstractmethod
    def remove(self, target):
        pass
    