# -*- coding: utf-8 -*-
# @Time    : 2020/10/11 0011 15:26
# @Author  : zhengwei
# @File    : 30.py
# @Software: PyCharm
import copy
class Solution:
    def findSubstring(self, s, words):
        m = len(words)
        n = len(words[0])
        i = 0
        results = []
        while i <= len(s) - m*n:
            temp = s[i:i+m*n]
            word = copy.deepcopy(words)
            for j in range(0, len(temp)-n+1, n):
                if temp[j:j+n] in word:
                    word.remove(temp[j:j+n])
                else:
                    break
            if len(word)==0:
                results.append(i)
            i=i+1
        return results
test = Solution()
result = test.findSubstring('barfoothefoobarman',['foo','bar'])
print(result)


