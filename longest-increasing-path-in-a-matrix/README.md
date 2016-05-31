Question - original [post](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/)
----------------------------------------------------------------------------------------------

Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

**Example 1:**

```
nums = [[9,9,4],
         ^
        [6,6,8],
         ^
        [2,1,1]]
         ^ ^
```

Return `4`
The longest increasing path is `[1, 2, 6, 9]`.

**Example 2:**

```
nums = [[3,4,5],
         ^ ^ ^
        [3,2,6],
             ^
        [2,2,1]]
```

Return `4`
The longest increasing path is `[3, 4, 5, 6]`. Moving diagonally is not allowed.

Solution - [link](answer.py)
----------------------------

The strategy is to do **Path Finding** algorithms (`DFS`, `BFS`, ...)
to every element. In order to make the path-finding process faster, you could apply the memorization technique from Dynamic Programming to it.

For example:

```
[[9,9,4],
 [6,6,8],
 [2,1,1]]
```

Graph of going through the possible paths:

![path finding](sample-01.png)

We can directly use the outcome from the previous visited paths. e.g: The `6->9` path was visited when searching the `2->6->...` path. That's why we need to memorize the visited paths.

Eventually, the problem is a composite problem of **Path Finding** and **Dynamic Programming**.

```python
class Solution(object):
    """
    Given an integer matrix, find the length of the longest increasing path.
    From each cell, you can either move to four directions: left, right, up or
    down.
    You may NOT move diagonally or move outside of the boundary (i.e.
    wrap-around is not allowed).
    """

    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        maxPath = 0
        # The boundary.
        if matrix:
            lenRow = len(matrix)
            lenCol = len(matrix[0])
            # Create a copy of the given matrix, where the elements are -1.
            visitedPath = [[0] * len(matrix[0]) for _ in range(len(matrix))]
            # Do DFS (or BFS, A*, ...whatever) to every element in the matrix.
            for row in range(lenRow):
                for col in range(lenCol):
                    maxPath = max(maxPath, self.doDFS(matrix,
                                                      lenRow - 1,
                                                      lenCol - 1,
                                                      None,
                                                      (row, col),
                                                      visitedPath))
            return maxPath
        else:
            return 0

    def doDFS(self, mat, maxRow, maxCol, prevPath, currPath, visitedPath):
        """
        :param mat: List[List[int]]
        :param prevPath: (row, col) tuple
        :param currPath: (row, col) tuple
        :param visitedPath: List[List[int]], the memorization matrix.
        longest increasing path as the value.
        :return: int, the longest increasing path.
        """
        # The current traversing row and col.
        currRow = currPath[0]
        currCol = currPath[1]

        if prevPath:
            prevRow = prevPath[0]
            prevCol = prevPath[1]
            if mat[prevRow][prevCol] >= mat[currRow][currCol]:
                # Stop when the value of current node isn't greater than the
                # previous one.
                return 0
        if visitedPath[currRow][currCol]:
            return visitedPath[currRow][currCol]

        # Keep going forward through the paths #################################
        # Look right.
        nextPath = (currRow, min(currCol + 1, maxCol))
        pathR = self.doDFS(mat, maxRow, maxCol, currPath, nextPath, visitedPath)
        # Look down.
        nextPath = (min(currRow + 1, maxRow), currCol)
        pathD = self.doDFS(mat, maxRow, maxCol, currPath, nextPath, visitedPath)
        # Look left.
        nextPath = (currRow, max(currCol - 1, 0))
        pathL = self.doDFS(mat, maxRow, maxCol, currPath, nextPath, visitedPath)
        # Look up.
        nextPath = (max(currRow - 1, 0), currCol)
        pathU = self.doDFS(mat, maxRow, maxCol, currPath, nextPath, visitedPath)

        # Going backward to the visited paths ##################################
        maxPath = max(max(pathR, pathD), max(pathL, pathU))
        if maxPath:
            visitedPath[currRow][currCol] = maxPath + 1
        else:
            visitedPath[currRow][currCol] = 1
        return visitedPath[currRow][currCol]
```

Application Sample
------------------
* To find the largest closing path from a given binary image.
