# -*- coding: utf-8 -*-
# @Time    : 2020/8/17 0017 20:20
# @Author  : zhengwei
# @File    : 9.py
# @Software: PyCharm


class Solution:
    def isPalindrome(self, x: int) -> bool:
        s1 = str(x)
        s2 = s1[::-1]
        if s1 == s2:
            return True
        else:
            return False



