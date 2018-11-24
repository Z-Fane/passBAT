# -*- coding:utf-8 -*-

class Rotation:
    def chkRotation(self, A, lena, B, lenb):
        # write code here
        end=A+A
        if B in end:
            return True
        else:
            return False