# -*- coding:utf-8 -*-

class Transform:
    def chkTransform(self, A, lena, B, lenb):
        a = self.saveDict(A, lena)
        b = self.saveDict(B, lenb)
        return a == b

    def saveDict(self, X, l):
        x_dict = {}
        for i in range(l):
            if X[i] not in x_dict:
                x_dict[X[i]] = 0
            x_dict[X[i]] += 1
        return x_dict


