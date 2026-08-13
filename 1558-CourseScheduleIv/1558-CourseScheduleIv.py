# Last updated: 8/13/2026, 8:21:37 PM
from collections import deque

class Solution(object):
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        # 1. Build adjacency list and track in-degrees
        graph = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        
        for pre, crs in prerequisites:
            graph[pre].append(crs)
            in_degree[crs] += 1
            
        # 2. Initialize a 2D matrix to track prerequisites
        # is_pre[u][v] will be True if 'u' is a prerequisite of 'v'
        is_pre = [[False] * numCourses for _ in range(numCourses)]
        
        # Queue for Kahn's algorithm (Topological Sort)
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        
        # 3. Process the graph in topological order
        while queue:
            curr = queue.popleft()
            
            for neighbor in graph[curr]:
                # Direct relationship
                is_pre[curr][neighbor] = True
                
                # Indirect/Transitive relationship: 
                # If 'i' is a prerequisite of 'curr', it's also a prerequisite of 'neighbor'
                for i in range(numCourses):
                    if is_pre[i][curr]:
                        is_pre[i][neighbor] = True
                        
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
                    
        # 4. Answer the queries
        result = []
        for u, v in queries:
            result.append(is_pre[u][v])
            
        return result