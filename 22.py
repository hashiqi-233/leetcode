# -*- coding: utf-8 -*-
# @Time    : 2020/9/26 0026 22:04
# @Author  : zhengwei
# @File    : 22.py
# @Software: PyCharm

class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.dfs(res, n, n, '')
        return res

    def dfs(self, res, left, right, path):
        if left == 0 and right == 0:
            res.append(path)
            return
        if left > 0:
            self.dfs(res, left - 1, right, path + '(')
        if left < right:
            self.dfs(res, left, right - 1, path + ')')

test = Solution()
result = test.generateParenthesis(3)
print(result)

        



