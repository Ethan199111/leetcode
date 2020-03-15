from list import ListNode


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        dummy_head = ListNode(0)
        curr = dummy_head
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                curr = curr.next
                l1 = l1.next
            else:
                curr.next = l2
                curr = curr.next
                l2 = l2.next
        while l1:
            curr.next = l1
            curr = curr.next
            l1 = l1.next
        while l2:
            curr.next = l2
            curr = curr.next
            l2 = l2.next
        return dummy_head.next
