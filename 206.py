# -*- coding: utf-8 -*-
# @Time    : 2020/10/8 0008 10:39
# @Author  : zhengwei
# @File    : 206.py
# @Software: PyCharm


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        pre = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre





