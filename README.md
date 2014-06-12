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
 - Merge Two Sorted Lists

#### LRUCache
 - 使用双向链表保存 cache 数据，使用 dict 来确定某个 key 是否存在
 - 每次 set 的时候，查看是否存在 key, 存在的话将这个 key 移动到 head，否则插入一个新的节点到 head
 - 当 size 大于 capacity，时删除最后的节点
 - 错了几次都是因为很多小细节没处理好

#### part4
 - Triangle
  - 到 n - 1 行时，最小值为 n - 1 行的数与下面两个最小的数的和
 - Path Sum
  - 到某个节点之后，递归判断两棵子树是否满足 sum - cur_node_val
  - 最开始只考虑到正数的情况，所以出错了
 - Sum Root to Leaf Numbers
  - 递归
 - Restore IP Addresses
 - N-Queens
  - DFS
 - N-Queens II

#### part5
 - Jump Game
  - 从第一步开始，把可以进入索引加入一个 set 中，排除自身之后再遍历这些索引
  - 以上是看错题的想法，扫一遍，看能到最远是什么
 - Jump Game II
  - 从零开始，看跳一步能到的区域是什么，再看跳两步能到的区域是什么
 - Permutations II
  - 递归
 - Unique Binary Search Trees
  - DP
  - 以不同的数当根节点的 BST 等于其左右子树的 BST 的乘积
 - Unique Paths
  - (i, j) = (i - 1, j) + (i, j -1)
 - Convert Sorted Array to Binary Search Tree
  - 确认中间节点之后，处理左右子树

#### part6
 - Path Sum II
  - 经过一个节点之后 sum - root.val 递归左右子树
  - 错了几次没处理负数的情况
 - removeDuplicates
 - Unique Paths II
  - 需要小心处理当前是否可达
