# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        visited_nodes = set()
        
        if head:
            visited_nodes.add(head)
            curr = curr.next

        while curr:
            if curr in visited_nodes:
                return True
            visited_nodes.add(curr)
            curr = curr.next
        
        return False
