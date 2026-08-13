# Last updated: 8/13/2026, 8:19:10 PM
class Solution(object):
    def findWordsContaining(self, words, x):
        ar=[]
        idx=0
        for index,word in enumerate(words):
            if x in word:
                ar.append(index)
                
        return ar

        