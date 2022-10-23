import functools
class Solution(object):
    def numMatchingSubseq(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: int
        """
        count = 0
        for word in words:
            if self.compareString(word, s): 
                count += 1
        return count
    
    @functools.lru_cache
    def compareString(self, word, s): # compare string method is problemetic
        if not s: return False # why return False
        i = 0
        j = 0
        while i < len(s) and j < len(word):
            if s[i] == word[j]:
                i += 1
                j += 1
            else:
                i += 1
            if j == len(word):
                return True
        return False
    
    # matching subsequence 这一类的题目怎么做？！！！
    