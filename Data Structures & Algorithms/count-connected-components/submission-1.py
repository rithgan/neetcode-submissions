class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not len(edges):
            return n
        graph = self.buildGraph(edges)
        visited = set()
        count = 0
        for node in graph:
            if self.explore(graph,node,visited):
                count+=1
        return count
            
    
    def buildGraph(self,edges):
        graph = {}
        for edge in edges:
            a,b=edge
            if a not in graph:
                graph[a]=[]
            if b not in graph:
                graph[b]=[]
            graph[a].append(b)
            graph[b].append(a)
        return graph
    
    def explore(self,graph,curr,visited):
        if curr in visited: return False
        visited.add(curr)
        
        for neighbhor in graph[curr]:
            self.explore(graph,neighbhor,visited)
            
        return True
