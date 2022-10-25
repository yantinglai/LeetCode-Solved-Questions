class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
     
        max_count = 0
        left = 0 
        right = 0
        check = set()
        
        # 经验：如果是涉及到这种要去重，有时候指针要动，有时候不要动的情况，最好就不要写for loop
        # 用 while loop是最好的，因为你可以决定究竟什么时候去移动这个指针！
        
        while right < len(s):
            while s[right] in check:
                check.remove(s[left])
                left += 1 # 先移除再动指针！！！
            if s[right] not in check:
                check.add(s[right])
                max_count = max(max_count, right - left + 1)
                right += 1
        return max_count
            
            
        # need left and right pointer
        # use set to to element in the set
        # loop through the string s
        # while the next character is in the set:
             # move the left pointer forward, until there is no duplicate
            # record the length of the set, using count and max_count
            