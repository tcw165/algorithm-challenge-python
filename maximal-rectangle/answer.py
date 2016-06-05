class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        maxArea = 0
        maxRow = len(matrix)
        maxCol = len(matrix[0])
        # For every row in the given 2D matrix, it is a "Largest Rectangle in
        # Histogram" problem, which is the sub-problem.
        lookupTable = [0 for _ in range(maxCol)]
        for row in range(maxRow):
            for col in range(maxCol):
                # If it is "1"
                if int(matrix[row][col]) > 0:
                    # Accumulate the column if if's 1's.
                    lookupTable[col] += int(matrix[row][col])
                else:
                    # Clean the column if it's 0's.
                    lookupTable[col] = 0
            # self.debugPrint(lookupTable)
            # Calculate the maximum area.
            maxArea = max(maxArea,
                          self.maximalRectangleInHistogram(lookupTable))
        return maxArea

    # def maximalRectangleInHistogram(self, histogram):
    #     """
    #     Calculate the maximum rectangle area in terms of a given histogram.
    #     (Ver.1)
    #     :param histogram: List[int]
    #     :return:  int
    #     """
    #     maxArea = 0
    #     size = len(histogram)
    #     # For every bar in the histogram, we go through the previous bars.
    #     for i in range(size):
    #         # Take current height as the minimum height.
    #         minH = histogram[i]
    #         for j in reversed(range(i)):
    #             # Return if it meets zero.
    #             if histogram[j] == 0:
    #                 break
    #             # Find the minimum height at the moment.
    #             minH = min(minH, histogram[j])
    #             # Calculate the area at the moment.
    #             area = minH * (i - j + 1)
    #             # Find out the maximum area.
    #             maxArea = max(maxArea, area)
    #     return maxArea

    def maximalRectangleInHistogram(self, histogram):
        """
        Calculate the maximum rectangle area in terms of a given histogram.
        (Ver.2)
        :param histogram: List[int]
        :return:  int
        """
        # Stack for storing the index.
        posStack = []
        i = 0
        maxArea = 0
        while i < len(histogram):
            if len(posStack) == 0 or histogram[i] > histogram[posStack[-1]]:
                # Advance the index when either the stack is empty or the
                # current height is greater than the top one of the stack.
                posStack.append(i)
                i += 1
            else:
                curr = posStack.pop()
                width = i if len(posStack) == 0\
                    else i - posStack[-1] - 1
                maxArea = max(maxArea, width * histogram[curr])
        # Clean the stack.
        while posStack:
            curr = posStack.pop()
            width = i if len(posStack) == 0\
                else len(histogram) - posStack[-1] - 1
            maxArea = max(maxArea, width * histogram[curr])
        return maxArea

    def debugPrint(self, historgram):
        out = [i for i in historgram]
        print str(out)


if __name__ == "__main__":
    sol = Solution()
    print "Given [0]\n," \
          "the answer is %d and expected answer is 0" % \
          sol.maximalRectangle(["0"])
    print "Given [1],\n" \
          "the answer is %d and expected answer is 1" % \
          sol.maximalRectangle(["1"])
    print "Given [11]\n," \
          "the answer is %d and expected answer is 2" % \
          sol.maximalRectangle(["11"])
    print "Given [1111,\n" \
          "       1111,\n" \
          "       1111]\n" \
          "the answer is %d and expected answer is 12" % \
          sol.maximalRectangle(["1111",
                                "1111",
                                "1111"])
    print "Given [10100,\n" \
          "       10111,\n" \
          "       11111,\n" \
          "       10010]\n" \
          "the answer is %d and expected answer is 6" % \
          sol.maximalRectangle(["10100",
                                "10111",
                                "11111",
                                "10010"])
    print "Given [101111,\n" \
          "       011111,\n" \
          "       011011,\n" \
          "       001111,\n" \
          "       101100]\n," \
          "the answer is %d and expected answer is 8" % \
          sol.maximalRectangle(["101111",
                                "011111",
                                "011011",
                                "001111",
                                "101100"])
