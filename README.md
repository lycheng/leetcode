leetcode
========

leetcode AC codes

problems: http://oj.leetcode.com/problems/

#### part1
 - reverseWords
  - 多注意处理空格
 - singleNumber
  - a ^ b ^ a = b
 - maxDepth
  - DFS
 - isSameTree
  - DFS
 - reverse number
  -这道题用 python 略犯规啊，它好心提示一点用都没有
 - hasCycle
  - 前面一个指针一次跳两个，后面一个指针一次跳一个，总会相遇
 - preorder && inorder
 - searchInsert
 - deleteDuplicates
 - climbStairs
  - 第一次用递归做超时，后面想了下，大概的思路是：到达某一个 n 可能的步数就是到达 n - 1 和到达 n - 2 的和

#### part2
 - maxSubArray
  - sum[i+1] = max(a[i+1], sum[i] + a[i+1])
  - result = max(result, sum[i])
 - removeElement
 - twoSum
  - 错了挺多次，最开始直接用 index 来找位置，没考虑到重复元素
