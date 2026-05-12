class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        point = {}
        for i in points:

            point[tuple(i)] = ((i[0])**2 + (i[1])**2)**0.5
        return sorted(point, key=point.get)[:k]