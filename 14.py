# -*- coding: utf-8 -*-
# @Time    : 2020/9/6 0006 10:16
# @Author  : zhengwei
# @File    : 14.py
# @Software: PyCharm

class Solution:
    def longestCommonPrefix(self, strs):
        public_s = []
        if len(strs) <= 0:
            return ''
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if i<=len(strs[j])-1 and strs[0][i] == strs[j][i] :
                    continue
                else:
                    return ''.join(public_s)
            public_s.append(strs[0][i])
        return ''.join(public_s)

test = Solution()
result = test.longestCommonPrefix(['flower','flow'])
print(result)







