# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        new_head = ListNode(0)
        current_new = new_head

        current = head.next  # start after the initial 0
        sum_between_zeros = 0

        while current is not None:
            if current.val == 0:
                # Create a new node with the sum and attach to the new list
                current_new.next = ListNode(sum_between_zeros)
                current_new = current_new.next  # move to the new node
                sum_between_zeros = 0  # reset sum
            else:
                sum_between_zeros += current.val
            current = current.next

        return new_head.next
            