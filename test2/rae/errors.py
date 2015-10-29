#!/usr/bin/env python
#-*-coding:utf-8-*-
'''

@author:    Wanglj
@date:  2015.10.25
'''

class UnexpectedStateError(Exception):
  
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return self.msg
  
class UnsupportedOperationError(Exception):
  
    def __init(self, msg):
        self.msg = msg
    
    def __str__(self):
        return self.msg
  
class GridentCheckingFailedError(Exception):
  
    def __init(self, msg):
        self.msg = msg
    
    def __str__(self):
        return self.msg