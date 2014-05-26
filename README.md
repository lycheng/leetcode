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
 - lengthOfLastWord
  - 空格处理啊
 - wordBreak
  - 将单词分为三部分，找出前缀和后缀，再继续找递归找中间的部分，第一次错误就是认为在两边用过的单词不能重用
 - maxProfit I
 - maxprofit II
  - 在上升的序列中，最低点买入和最高点卖出跟每次买入卖出获利是一样的
 - plusOne
  - 囧，忘了去掉 print 就超时了

#### part3
 - swapPairs
  - 维护三个指针
 - Populating Next Right Pointers in Each Node
  - 先连接某个节点的子树，再连接该节点的左子树的右子树与该节点的右子树的左子树，再往下递归即可
 - Permutations
  - 确定第一个数，然后递归剩下的组合，无重复
