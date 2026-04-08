class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses = {i:[] for i in range(numCourses)}
        for curr, preq in prerequisites:
            courses[curr].append(preq)
        
        visited = set()
        order = []
        
        def dfs(curr):
            if curr in visited:
                return []
            if courses[curr] == [] and curr not in order:
                order.append(curr)
            
            visited.add(curr)
            for pre in courses[curr]:
                if not dfs(pre):
                    return []
            visited.remove(curr)
            courses[curr] = []
            if curr not in order:
                order.append(curr)
            return order 


           




        


        
        for c in range(numCourses):
            if dfs(c) == []:
                return []
        else:
            return order
