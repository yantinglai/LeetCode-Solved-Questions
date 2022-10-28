class Solution(object):
    def findReplaceString(self, s, indices, sources, targets):
        """
        :type s: str
        :type indices: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        if indices[0] == indices[1]: return s
        res = []
        ptr = 0
        for idx, source, target in sorted(zip(indices, sources, targets)):
            res.append(s[ptr:idx])
            check_string = s[idx: idx + len(source)]
            if check_string == source:
                res.append(target)
            else:
                res.append(check_string)
            ptr = idx + len(source)
        res.append(s[ptr:])
        return "".join(res)
            
            
            