# -*- coding:utf-8 -*-
class Replacement:
    def replaceSpace(self, iniString, length):
        s = ''
        for l in iniString:
            if l == ' ':
                l = '%20'
            s = s + l
        return s