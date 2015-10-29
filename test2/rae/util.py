#!/usr/bin/env python
#-*-coding:utf-8-*-
'''

@author:    Wanglj
@date:  2015.10.25
'''
from numpy import sqrt
from numpy.random import rand

__all__ = ['init_W', 'init_We']

def init_W(row, col, return_row_vector=True):
    '''Initialize weight matrix.
  
    Args:
        row: number of rows
        col: number of columns
        return_row_vector: whether return a row vector or not
    
    Returns:
        An numpy.array of size row*col 
    '''
    r = sqrt(6) / sqrt((row+1) + (col+1)) # 1 : for bias
    if return_row_vector:
        return rand(row*col) * 2 * r - r
    else:
        return rand(row, col) * 2 * r - r