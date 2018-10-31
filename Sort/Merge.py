# -*- coding:utf-8 -*-
class Merge:
    def mergeAB(self, A, B, n, m):
        indexA=n-1
        indexB=m-1
        indexM=n+m-1
        while indexA>=0 and indexB>=0 and indexM>=0:
            if A[indexA]>B[indexB]:
                A[indexM]=A[indexA]
                indexM-=1
                indexA-=1
            else:
                A[indexM]=B[indexB]
                indexM-=1
                indexB-=1
        if indexB>=0:
            A[:indexM+1]=B[:indexB+1]
            indexM-=1
            indexB-=1
        return A