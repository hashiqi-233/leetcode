# -*- coding: utf-8 -*-
# @Time    : 2020/8/10 0010 20:10
# @Author  : zhengwei
# @File    : 5.py
# @Software: PyCharm

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == None:
            return None
        l = len(s)
        if l<= 1:
            return s
        long_s = ''
        # 从第一个字符开始遍历，找到所有的组合然后判断是不是回文串，保存最长的回文串
        for i in range(l):
            for j in range(i, l+1):
                tmp_s = s[i:j]
                reverse_s = tmp_s[::-1]
                if tmp_s == reverse_s:
                    if len(tmp_s) > len(long_s):
                        long_s = tmp_s
        return long_s

test = Solution()
result = test.longestPalindrome('bb')
print(result)







