
from typing import List


class Solution:
    def MinimumEffort(self, rows : int, columns : int, heights : List[List[int]]) -> int:
        # code here
        from heapq import heappush, heappop
        
        costs = {(0, 0): 0}
        q = [(0, 0, 0)]
        while q:
            cost0, r0, c0 = heappop(q)
            if (r0, c0) == (rows-1, columns-1):
                return cost0
                
            for (dr, dc) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                r = r0+dr
                c = c0+dc 
                if r < 0 or r >= rows or c < 0 or c >= columns:
                    continue
                cost = max(cost0, abs(heights[r0][c0]-heights[r][c]))
                if (r, c) not in costs or costs[r, c] > cost:
                    heappush(q, (cost, r, c))
                    costs[r, c] = cost
        return -1
        



#{ 
 # Driver Code Starts
class IntMatrix:

    def __init__(self) -> None:
        pass

    def Input(self, n, m):
        matrix = []
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix

    def Print(self, arr):
        for i in arr:
            for j in i:
                print(j, end=" ")
            print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        rows = int(input())

        columns = int(input())

        heights = IntMatrix().Input(rows, columns)

        obj = Solution()
        res = obj.MinimumEffort(rows, columns, heights)

        print(res)

# } Driver Code Ends