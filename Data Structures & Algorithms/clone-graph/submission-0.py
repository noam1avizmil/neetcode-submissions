"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        cloned ={}
        def dfs(neighbor: Optional['Node']) -> Optional['Node']:
            if neighbor in cloned:
                return cloned[neighbor]
            new_n = Node(neighbor.val)
            cloned[neighbor] = new_n
            for i in neighbor.neighbors:
                new_n.neighbors.append(dfs(i))
            return new_n
        if node is  None:
            return None
        else:
            return dfs(node)
        

        