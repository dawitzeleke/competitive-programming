from math import sqrt
class Solution(object):
    def kClosest(self, points, k):
        dist_points = []
        for point in points:
            distance = sqrt(sum([i**2 for i in point]))
            dist_points.append((distance, point))
     
        dist_points.sort()
        
        return [point for dist, point in dist_points[:k]] 
