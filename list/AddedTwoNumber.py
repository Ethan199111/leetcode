from list import ListNode


class Solution:

    @staticmethod
    def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:

        if not l1:
            return l2
        if not l2:
            return l1

        dummy_head = ListNode(0)
        curr = dummy_head
        c = 0
        while l1 and l2:
            total = l1.val + l2.val + c
            c = total // 10
            curr.next = ListNode(total % 10)
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            total = l1.val + c
            c = total // 10
            curr.next = ListNode(total % 10)
            curr = curr.next
            l1 = l1.next
        while l2:
            total = l2.val + c
            c = total // 10
            curr.next = ListNode(total % 10)
            curr = curr.next
            l2 = l2.next
        if c > 0:
            curr.next = ListNode(c)
        return dummy_head.next


l1 = ListNode(2)
l1.next = ListNode(5)

l2 = ListNode(3)
l2.next = ListNode(4)

res = Solution.addTwoNumbers(l1, l2)
print(ListNode.print(res))
