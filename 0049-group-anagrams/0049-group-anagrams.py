class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # if you sort a str, the return value will be a list
        # so you need to turn it back to a string with join method
        
        res = []
        d = collections.defaultdict()
        for word in strs:
            key_word = "".join(sorted(word))
            # print("key_word",key_word)
            if key_word not in d:
                d[key_word] = [word]
            else:
                d[key_word].append(word)
        
        return d.values()
            