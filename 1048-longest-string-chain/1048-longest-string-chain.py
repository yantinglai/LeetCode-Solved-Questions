class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words.sort(key = len) # 根据长度来sort这个words list
        d = collections.defaultdict(int)
        for word in words:
            d[word] = 1
            
        for word in words:
            cur_word = word
            for i in range(len(cur_word)):
                prev_word = cur_word[:i] + cur_word[i+1:]
                if prev_word in d:
                    d[cur_word] = max(d[prev_word]+1, d[cur_word])
        return max(d.values())
        
        # a:1
        # b:1
        # ba:2
        # bca:3
        # bda:3
        # bdca:4