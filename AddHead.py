"""
 Insert Node at the begining of a linked list
 head input could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""


def Insert(head, data):
    if head is None:
        node = Node(data)
        head = node
        return head
    node= Node(data)
    node.next = head
    head = node
    return head
