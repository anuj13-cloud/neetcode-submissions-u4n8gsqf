"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashMap = {}
        if not head:
            return None
        node = Node(head.val)
        first = head
        copy = node
        hashMap[head] = copy
        while first.next:
            copy.next = Node(first.next.val)
            first = first.next
            copy = copy.next
            hashMap[first] = copy
        copy = node
        while head:
            if head.random:
                copy.random = hashMap[head.random]
            else:
                copy.random = None

            head = head.next
            copy = copy.next
        return node 

        



        