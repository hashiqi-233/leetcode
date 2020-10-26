# -*- coding: utf-8 -*-
# @Time    : 2020/8/8 0008 22:31
# @Author  : zhengwei
# @File    : 3.py
# @Software: PyCharm

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        long_str = 0
        cur_str = []
        j = 0
        while j <= len(s) - 1:
            cur_str.append(s[j])
            if len(cur_str) == len(set(cur_str)):
                j = j + 1
            else:
                if len(cur_str) - 1 > long_str:
                    long_str = len(cur_str) - 1
                for k in range(len(cur_str) - 1):
                    if cur_str[k] == cur_str[-1]:
                        break
                cur_str = cur_str[k + 1:]
                j = j + 1
        if len(cur_str) > long_str:
            long_str = len(cur_str)
        return long_str


test = Solution()
result = test.lengthOfLongestSubstring('dvdf')
print(result)
