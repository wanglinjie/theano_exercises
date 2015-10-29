#!/usr/bin/env python
#-*-coding:utf-8-*-
'''

@author:    Wanglj
@date:  2015.10.25
'''
import time

class Timer(object):
  
    def tic(self):
        self.start = time.time()
    
    def toc(self):
        return time.time() - self.start