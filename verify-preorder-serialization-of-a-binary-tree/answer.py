class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        # The number of middle nodes.
        midNo = 0
        # The number of leaf nodes.
        leafNo = 0
        # If the binary tree is closed, there should be no more remaining nodes.
        isClosed = False
        
        for char in preorder.split(','):
            if isClosed:
                return False
        
            if char == '':
                return False
            elif char == '#':
                leafNo += 1
            else:
                midNo += 1
                # Reset the NULL accumulation.
                nullAccum = 0
            # The number of leaf nodes must not be greater than midNo + 1.
            if leafNo == midNo + 1:
                isClosed = True
            elif leafNo > midNo + 1:
                return False
        
        # The total number of nodes is 2n - 1, given n is the number of leaf
        # nodes.
        # print "midNo = ", midNo
        # print "leafNo = ", leafNo
        if midNo != leafNo - 1:
            return False
        else:
            return True

if __name__ == "__main__":
    sol = Solution()
    print "You answer is %s and it should be true" % (sol.isValidSerialization("9,#,92,#,#"))
    print "You answer is %s and it should be false" % (sol.isValidSerialization("9,#,#,#,92"))
    print "You answer is %s and it should be true" % (sol.isValidSerialization("9,#,93,#,9,9,#,#,#"))
    print "You answer is %s and it should be false" % (sol.isValidSerialization("#,7,6,9,#,#,#"))