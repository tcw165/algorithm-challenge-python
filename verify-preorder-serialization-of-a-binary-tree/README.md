Question - [post](https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/)
--------

One way to serialize a binary tree is to use pre-order traversal. When we encounter a non-null node, we record the node's value. If it is a null node, we record using a sentinel value such as `#`.

```
     _9_
    /   \
   3     2
  / \   / \
 4   1  #  6
/ \ / \   / \
# # # #   # #
```

For example, the above binary tree can be serialized to the string `"9,3,4,#,#,1,#,#,2,#,6,#,#"`, where `#` represents a null node.

Given a string of comma separated values, verify whether it is a correct preorder traversal serialization of a binary tree. Find an algorithm without reconstructing the tree.

Each comma separated value in the string must be either an integer or a character `'#'` representing null pointer.

You may assume that the input format is always valid, for example it could never contain two consecutive commas such as `"1,,3"`.

#### Example 1:

`"9,3,4,#,#,1,#,#,2,#,6,#,#"` Return `true`

#### Example 2:

`"1,#"` Return `false`

#### Example 3:

`"9,#,#,1"` Return `false`

---

Solution - [code](answer.py)
--------

In general, you could start with by sorting the given list for almost every algorithm problem. But it's an **order-sensitive** problem, so don't sort it. You might need to think about if the problem is a `dynamic programming` problem or could be solved by `divide and conquer` strategy. Apparently, it's neither.

The point to solve it is to make sure the formula, `midNo = leafNo - 1`, be fulfilled, where the `midNo` is the number of the middle nodes and the `leafNo` is the number of the leaf nodes. So you could go through the elements delimited by `','` by checking the `midNo` and `leafNo`. Since it's serialized in **pre-order**, the `leafNo` must not greater than the `midNo`, saying `leafNo < midNo - 1`. And if it happens to fulfill the formula, `midNo = leafNo - 1`, the tree is closed and there should be no more remaining nodes.

```python
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
```

---

Application Sample
------------------

Yet know.
