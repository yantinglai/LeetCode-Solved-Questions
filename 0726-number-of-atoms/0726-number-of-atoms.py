class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        stack = [collections.Counter()]
        n = len(formula)
        i = 0
        while i < n:
            c = formula[i]
            if c == "(":
                stack.append(collections.Counter())
                i += 1
            elif c == ")":
                cur_counter = stack.pop() # step1: get the cur_counter
                # find the mulfiplier after the ")"
                i += 1 # 跳过右括号
                start = i 
                while i < n and formula[i].isdigit():
                        i += 1
                multiplier = int(formula[start:i]) if formula[start:i] else 1
                
                for atom in cur_counter:
                    count = cur_counter[atom]
                    stack[-1][atom] += count * multiplier
            else:
                # find the normal atom case:
                atom = c
                i += 1
                start = i
                while i < n and formula[i].islower():
                    i += 1
                atom += formula[start:i]
                # find the number
                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                count = int(formula[start:i]) if formula[start:i] else 1
                
                stack[-1][atom] += count
        
        res = ""
        counter = stack[-1]
        
        for atom in sorted(counter):
            res += atom
            
            if counter[atom] > 1:
                res += str(counter[atom])
                    
        return res
         

        # int could be > one single digit
        # 找到第一个左括号，找到下一个右括号，找到括号外面的数字
        # 找到这样的第一组，就直接出栈，进行处理
        # need a stack, loop through the string array
        # need way to differentiate number and letters
        
        # 如何区分大小写字母？ord(formula[i]) - ord('a') < 0 - means it's Upper
        
   
        