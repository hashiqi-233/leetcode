# -*- coding: utf-8 -*-
# @Time    : 2020/10/18 0018 14:18
# @Author  : zhengwei
# @File    : 32.py
# @Software: PyCharm

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s: return 0

        stack = []
        ans = 0
        for i in range(len(s)):
            # 入栈条件
            if not stack or s[i] == '(' or s[stack[-1]] == ')':
                stack.append(i)     # 下标入栈
            else:
                # 计算结果
                stack.pop()
                ans = max(ans, i - (stack[-1] if stack else -1))
        return ans

test = Solution()
result = test.longestValidParentheses('(()')
print(result)




