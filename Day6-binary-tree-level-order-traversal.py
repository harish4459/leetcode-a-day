Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000


Solution -

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res =[]
        queue = collections.deque()
        queue.append(root)
        while queue:
            qLen = len(queue)
            level =[]
            for i in range(qLen):
                curr = queue.popleft()
                if curr:
                    level.append(curr.val)
                    queue.append(curr.left)
                    queue.append(curr.right)
            if level:        
                res.append(level)
        return res
            
