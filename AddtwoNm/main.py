#addTwoNumbers leetcode question
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        res = []
        while l1 or l2 or carry:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0

            total = a+b+carry
            res.append(total%10)
            carry = total //10
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

            dummy = ListNode(0)
            curr = dummy
            for num in res:
                curr.next = ListNode(0)
                curr = curr.next
            return dummy.next
