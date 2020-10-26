# -*- coding: utf-8 -*-
# @Time    : 2020/8/24 0024 19:03
# @Author  : zhengwei
# @File    : 10.py
# @Software: PyCharm


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        is_matched = False
        i = 0
        j = 0
        while j <= len(p) - 1 and i <= len(s)-1:
            if s[i] == p[j]:
                i = i + 1
                j = j + 1
            elif p[j] == '.':
                i = i + 1
                j = j + 1
            elif p[j] == '*':
                if s[i] == s[i - 1] and s[i - 1] == p[j - 1]:
                    i = i + 1
                elif p[j - 1] == '.':
                    i = i + 1
                    j = j - 1
                else:
                    j = j + 1
            else:
                j = j + 1
        if i >= len(s):
            is_matched = True
        return is_matched


test = Solution()
result = test.isMatch('ab', '.*c')
print(result)
