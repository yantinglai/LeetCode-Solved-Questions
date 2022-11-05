class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        cur_line = []
        res = []
        total_word = 0
        for word in words:
            if len(word) + len(cur_line) - 1 + total_word >= maxWidth:
                for i in range(maxWidth - total_word):
                    cur_line[i % max(1,len(cur_line)-1)]  += " "
                 
                res.append("".join(cur_line))
                cur_line = []
                total_word = 0
          
            cur_line.append(word)
            total_word += len(word)
                
        return res + [' '. join(cur_line).ljust(maxWidth)]
        
                
