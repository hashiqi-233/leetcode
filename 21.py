# -*- coding: utf-8 -*-
# @Time    : 2020/9/26 0026 20:51
# @Author  : zhengwei
# @File    : 21.py
# @Software: PyCharm


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1, l2):
        l1_result = []
        l2_result = []
        while l1:
            l1_result.append(l1.val)
            l1 = l1.next
        while l2:
            l2_result.append(l2.val)
            l2 = l2.next
        result = l1_result + l2_result
        result.sort()
        p = ListNode(0)
        l = p
        for i in range(len(result)):
            l.next = ListNode(result[i])
            l = l.next
        return p.next


