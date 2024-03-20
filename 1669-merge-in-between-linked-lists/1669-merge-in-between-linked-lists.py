# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        """
        :type list1: ListNode
        :type a: int
        :type b: int
        :type list2: ListNode
        :rtype: ListNode
        """
        current = list1
        for _ in range(a - 1):
            current = current.next
        
        # Find the bth node
        temp = current
        for _ in range(b - a + 2):
            temp = temp.next
        
        # Connect ath node to the head of list2
        current.next = list2
        
        # Find the end of list2
        while list2.next:
            list2 = list2.next
        
        # Connect the end of list2 to the b+1th node
        list2.next = temp
        
        return list1