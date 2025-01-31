import sys
from idlelib.tree import TreeNode
from typing import Optional, List

# input = sys.stdin.readline
#
# def solution():
#     n = int(input())
#     balls_str = input().strip()
#
#     r_to_right = balls_str.rstrip('R').count('R')
#     r_to_left = balls_str.lstrip('R').count('R')
#
#     b_to_right = balls_str.rstrip('B').count('B')
#     b_to_left = balls_str.lstrip('B').count('B')
#
#     sys.stdout.write(f"{min(r_to_right, r_to_left, b_to_right, b_to_left)}")
#
#
# solution()


# Leetcode 102. Binary Tree Level Order Traversal
class Solution:
    def levelOrder(self, root) -> List[List[int]]:

        tree = []
        cnt = 0
        k = 1
        for i in range(len(root)):
            if i == 0:
                tree.append([root[i]])
            else:
                if cnt == 0:
                    tree.append([])
                if type(root[i]) is int:
                    tree[-1].append(root[i])

                cnt += 1
            if cnt == 2**k:
                k += 1
                cnt = 0

        return tree

print(Solution().levelOrder([3,9,20,'null','null',15,7]))