# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        n = head
        while n.next != None:
            if n.val != "Visited":
                n.val = "Visited"
                n = n.next
            else:
                return n