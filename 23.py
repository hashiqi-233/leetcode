# -*- coding: utf-8 -*-
# @Time    : 2020/10/6 0006 18:32
# @Author  : zhengwei
# @File    : 23.py
# @Software: PyCharm

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists):
        results = []
        for list1 in lists:
            while list1:
                results.append(list1.val)
                list1 = list1.next
        results.sort()
        head = ListNode(0)
        l = head
        for i in results:
            l.next = ListNode(i)
            l = l.next
        return head.next








