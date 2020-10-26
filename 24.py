# -*- coding: utf-8 -*-
# @Time    : 2020/10/8 0008 9:54
# @Author  : zhengwei
# @File    : 24.py
# @Software: PyCharm

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head):
        thead = ListNode(0)
        thead.next = head
        c = thead
        while c.next and c.next.next:
            a = c.next
            b = c.next.next
            c.next = b
            a.next = b.next
            b.next = a
            c = c.next.next
        return thead.next




