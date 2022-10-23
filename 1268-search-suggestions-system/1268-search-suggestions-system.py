class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        # common prefix with searchWord -
        
        # sort products based on lexicographical order 
        
        products.sort()
        res = []
        
        for i in range(1, len(searchWord)+1):
            match_str = searchWord[:i]
            # print(match_str)
            path = []
            for product in products:
                if match_str == product[:i]:
                    path.append(product)
                    # print("path",path,"match_str",match_str,"product",product)
            res.append(path[:3])
        return res
                
                    