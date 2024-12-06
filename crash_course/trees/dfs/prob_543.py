"""
Diameter of binary tree
given the root of tree return the diameter of the tree

"""

def diameterTree(root):
    """Method that returns the length of the diameter of the tree"""
    def diameterOfBinaryTree(self, root) -> int:
        """USE dfs approach"""

        self.diameter = 0

        def dfs(current):
            if not current:
                return 0
            
            left_h = dfs(current.left)
            right_h = dfs(current.right)

            self.diameter = max(self.diameter, (left_h + right_h))

            return max(left_h, right_h) + 1

        dfs(root)
        return self.diameter



