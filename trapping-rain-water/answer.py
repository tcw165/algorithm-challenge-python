class Solution(object):
    # def trap(self, heights):
    #     if not heights or len(heights) < 3:
    #         return 0
    #
    #     size = len(heights)
    #     lBound = [0] * size
    #     rBound = [0] * size
    #
    #     h = heights[0]
    #     for i in range(size):
    #         lBound[i] = h = max(h, heights[i])
    #
    #     h = heights[size - 1]
    #     for i in reversed(range(size)):
    #         rBound[i] = h = max(h, heights[i])
    #
    #     water = 0
    #     for i in range(size):
    #         water += min(lBound[i], rBound[i]) - heights[i]
    #
    #     return water


    def trap(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights or len(heights) < 3:
            return 0

        level = water = 0
        i = 0
        j = len(heights) - 1
        while i < j:
            # Take the lower side as the current ground level.
            it = heights[i if heights[i] < heights[j] else j]
            # Advance the lower side close to the higher side.
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1

            if level > it:
                # If the ground level is lower than the water level, fill it
                # with the water.
                water += level - it
            else:
                # Update the water level.
                level = it
        return water


if __name__ == "__main__":
    sol = Solution()
    print "Given [0,1,0,2,1,0,1,3,2,1,2,1], " \
          "the answer is %s and the expected answer is 6" % \
          sol.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
