# -*- coding: utf-8 -*-
# @Time    : 2020/10/10 0010 21:22
# @Author  : zhengwei
# @File    : 28.py
# @Software: PyCharm

class Solution:
    def strStr(self, haystack, needle):
        if len(needle) == 0:
            return 0
        i = 0
        while i <= len(haystack)-len(needle):
            if haystack[i] == needle[0]:
                if haystack[i:i+len(needle)] == needle:
                    return i
                else:
                    i = i + 1
            else:
                i = i + 1
        return -1

test = Solution()
result = test.strStr('mississippi','issip')
print(result)



