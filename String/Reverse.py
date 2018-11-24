# -*- coding:utf-8 -*-

class Reverse:

    def reverseSentence(self, A, n):
        # 句子整体逆序
        tmp_s=self.reverse(A,0,n-1)
        # 单词逆序
        l=0
        r=-1
        for i in range(n-1):
            if tmp_s[i] != ' ':
                r=i-1
                self.reverse(tmp_s,l,r)
                l=i+1
            elif i==n-1:
                r=i
                self.reverse(tmp_s,l,r)
        return tmp_s

    def reverse(self, s, start, end):
        for i in range(start, end):
            tmp = s[start]
            s[start] = s[end]
            s[end] = tmp
            start += 1
            end -= 1
        return s
