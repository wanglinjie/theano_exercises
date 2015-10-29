#!/usr/bin/env python
#-*-coding:utf-8-*-
'''

@author:    Wanglj
@date:  2015.10.25
'''

class Instance(object):
    '''A reordering training example'''
  
    def __init__(self, words):
        '''
        Args:
            words: numpy.array (an int array of word indices)
        '''
        self.words = words

    def __str__(self):
        parts = []
        parts.append(' '.join([str(i) for i in self.words]))
        return parts
    
    @classmethod
    def parse_from_str(cls, line, word_vector):
        '''The format of the line should be like the following:
        src_word1, src_word2,..., src_wordn ||| freq
        '''
        words = [word_vector.get_word_index(word) for word in line[:].split()]

        return Instance(words)