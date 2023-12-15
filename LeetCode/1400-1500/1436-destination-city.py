class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        graph = {}
        unique = []
        for p in paths:
            unique.append(p[0])
            unique.append(p[1])
            graph[p[0]] = p[1]
        s = set(graph.keys()).symmetric_difference(set(unique))
        return list(s)[0]
        
        
