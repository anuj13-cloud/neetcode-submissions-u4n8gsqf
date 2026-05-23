class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {c: [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        output = []
        visit = set()

        def dfs(crs):
            if crs in visit:
                return False
            if prereq[crs] ==[]:
                if crs not in output:
                    output.append(crs)

                return True

            visit.add(crs)
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False
            visit.remove(crs)
            prereq[crs] = []
            output.append(crs)
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output