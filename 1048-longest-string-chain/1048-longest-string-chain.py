class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # sort - increasing order (len)
        # a: 1
        # b: 1
        # ba:1 +1
        # bca: 3
        # bda: 1
        # bdca:4
        words.sort(key = len)
        d = collections.defaultdict(int)
        for word in words:
            d[word] = 1
        
        for word in words:
            for i in range(len(word)):
                substring = word[:i] + word[i+1:]
                if substring in d:
                    d[word] = max(d[word], d[substring] + 1)
        return max(d.values())
        
        
    
    
                
        
        
        
        
        
       