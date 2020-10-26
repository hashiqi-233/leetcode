# -*- coding: utf-8 -*-
# @Time    : 2020/8/6 0006 22:35
# @Author  : zhengwei
# @File    : 2.py
# @Software: PyCharm

# Definition for singly-linked list.


Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 这里输入的l1和l2并不是头节点，而是头结点指向的下一个节点
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        results = []
        p1 = l1
        p2 = l2
        div = 0
        start_value = p1.val + p2.val+div
        div = start_value // 10
        mod = start_value % 10
        results.append(mod)
        while p1.next != None or p2.next != None:
            if p1.next != None and p2.next != None:
                tmp = p1.next.val + p2.next.val + div
                div = tmp // 10
                mod = tmp % 10
                results.append(mod)
                p1 = p1.next
                p2 = p2.next
            elif p1.next != None and p2.next == None:
                tmp = p1.next.val + div
                div = tmp // 10
                mod = tmp % 10
                results.append(mod)
                p1 = p1.next
            elif p1.next == None and p2.next != None:
                tmp = p2.next.val + div
                div = tmp // 10
                mod = tmp % 10
                results.append(mod)
                p2 = p2.next
        if div > 0:
            results.append(div)

        # 将列表转换为链表
        head = ListNode(0)
        p = head
        for i in range(len(results)):
            p.next = ListNode(results[i])
            p = p.next
        return head.next

l1 = ListNode(0)
l1.next = ListNode(2)
l1.next.next = ListNode(4)
l1.next.next.next = ListNode(3)
l2 = ListNode(0)
l2.next = ListNode(5)
l2.next.next = ListNode(6)
l2.next.next.next = ListNode(4)
test = Solution()
result = test.addTwoNumbers(l1, l2)
# print(result)
print(result.val, result.next.val, result.next.next.val)
