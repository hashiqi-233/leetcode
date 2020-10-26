# -*- coding: utf-8 -*-
# @Time    : 2020/10/8 0008 10:21
# @Author  : zhengwei
# @File    : 25.py
# @Software: PyCharm

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 翻转一个子链表，并且返回新的头与尾
    def reverse(self, head: ListNode, tail: ListNode):
        pre = tail.next
        cur = head
        while pre != tail:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return tail, head

    def reverseKGroup(self, head, k):
        hair = ListNode(0)
        hair.next = head
        pre = hair

        while head:
            tail = pre
            # 查看剩余部分长度是否大于等于 k
            for i in range(k):
                tail = tail.next
                if not tail:
                    return hair.next
            nex = tail.next
            head, tail = self.reverse(head, tail)
            # 把子链表重新接回原链表
            pre.next = head
            tail.next = nex
            pre = tail
            head = tail.next
        return hair.next




