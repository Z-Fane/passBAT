# -*- coding:utf-8 -*-

class DistinctSubstring:
    def longestSubstring(self, A, n):
        # write code here
        if A == None:
            return 0
        if len(A) == 1 and A[0] >= 'a' and A[0] <= 'z':
            return 1
        max_len = 0
        pre = -1  # 记录当前无重复子串的起始位置
        pos = [-1 for i in range(256)] # 记录字符上一次出现的位置
        for i in range(0, n):
            # 当前无重复子串起始位置=（当前第i个字符上一次出现的位置）与 （上一个无重复子串开始的位置）中大的。
            pre = max(pre, pos[ord(A[i])])
            # 当前无重复子串长度=当前位置-当前无重复我子串开始的位置
            cur_len=i-pre
            # 当前无重复子串的长度（i-pre） 与最长的无重复子串长度比较
            max_len = max(max_len, cur_len)
            # 记录第i个字符本次出现的位置
            pos[ord(A[i])] = i
        return max_len
