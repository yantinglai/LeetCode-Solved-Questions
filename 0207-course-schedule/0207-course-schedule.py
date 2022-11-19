class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = defaultdict(list)
        for cur,pre in prerequisites:
            d[pre].append(cur)
     
        
        m = defaultdict(list)
        for item in prerequisites:
            if item[0] not in m:
                m[item[0]] = [item[1]]
            else:
                m[item[0]].append(item[1])
      

        arr = [0 ] * (numCourses)
        for key in m:
            arr[key] = len(m[key])
        
        q = []
        n = numCourses 
        for i in range(len(arr)):
            if arr[i] == 0:
                q.append(i)  #  0,1,2
     
        
        while q:
            node = q.pop(0)
            for item in d[node]:
                arr[item] -= 1
                if arr[item] == 0:
                    q.append(item)
      
        
        for i in range(len(arr)):
            if arr[i] != 0: return False
        return True
     
        