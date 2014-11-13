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
 - Symmetric Tree
  - 递归处理 left.left == right.right and left.right == right.left
 - Minimum Depth of Binary Tree
  - 错了四次，想用 BFS 的做法去看，然后发现写起来很不直观，改成用递归的做法
 - Interleaving String
  - match[i][j] 表示 s1 的前 i 项和 s2 的前 j 项能否组合成字符串
 - Distinct Subsequences
  - DP，状态转移画图会比较清晰点

#### part7
 - Decode Ways
  - DP，奇怪的样例 01 不当作争取的数字
 - Remove Nth Node From End of List
  - 一个指针领先几步，然后和落后的指针一起行动，领先的指针到达结尾的时候后面的指针到达需要删除的节点的前一个节点，注意处理头节点
 - remove duplicates II
 - level order
  - 树的 BFS
 - Add Binary
  - 补前导零，然后模拟进位
 - Merge Sorted Array
  - 从后开始进行比较
 - Simplily Path
 - Rotate List
  - k 有可能比链表长度大
 - Binary Tree Level Order Traversal II
  - level order
 - Balanced Binary Tree
  - 开始用一个内部函数的时候死活 runtime error，后来发现使用类函数就可以

#### part8
 - Rotate Image
  - 先沿对角线翻转，然后上下翻转
 - Remove Duplicates from Sorted List II
  - 额外使用一个头节点
 - Validate Binary Search Tree
  - 左子树的最大值不得超过根节点，右子树的最小值不得小于根节点
  - 中序遍历一次，然后看下是不是递增
 - Binary Tree Postorder Traversal
 - Candy
  - 正向扫一遍处理递增的情况，反向扫一遍处理递减的情况
 - Spiral Matrix II
  - 从外面一环一环循环进来，注意处理坐标
 - Linked List Cycle II
  - http://fisherlei.blogspot.hk/2013/11/leetcode-linked-list-cycle-ii-solution.html
 - Pascal's Triangle II
  - 使用一个 list 保存上次运行的结果，从后往前加
 - Search in Rotated Sorted Array
  - A[mid] 比 A[l] 大的话，[l, mid] 处于递增序列
  - A[mid] 比 A[l] 小的话，mid 处于第二个递增序列
  - 两种情况分开判断即可

#### part9
 - Insertion Sort List
  - 检查如果是升序的话就不处理，遇到第一个不是升序的元素就从头开始找插入点
 - Gray Code
  - gray code = (binary code << 1) ^ binary code
 - Single Number II
  - 计算所有数每一位上的 1 的个数，余 3 之后就是只有一个数的那个数在该位上的值
  - 注意最后的 Two's complement 的转化 -B = ~B + 1
 - Container With Most Water
  - 最大的容积跟最短的线有关
 - Divide Two Integers
 - Set Matrix Zeroes
  - 先判断第一列第一行需不需要清零
  - 再用第一行第一列保存临时结果
  - 最后再清理第一行第一列
 - Longest Palindromic Substring
  - 可用动态规划，但写出来的会超时 Orz
  - 另一种就是计算每个以 i 为中心节点（分奇偶长度的子串的情况）的最长回文
 - Combinations
 - Populating next right pointers in each node ii
  - 每个递归找到当前层级最靠近目前节点的左下级节点或者右下级节点
  - 当前的节点的右下级节点 next 就确定了
  - 左下级节点也可以确定了
  - 递归从右子树开始

#### part10
  - Binary Tree Zigzag Level Order Traversal
  - Subsets
  - Subsets II
  - Reverse Linked List II
  - Letter Combinations of a Phone Number
  - Longest Consecutive Sequence
   - 通过 visited 保存每个节点是否访问过
   - 每访问一个未访问过的节点找出其所在的最大连续段的长度
  - Construct Binary Tree from Inorder and Postorder Traversal
  - Construct Binary Tree from Preorder and Inorder Traversal
   - 两题都一样，通过 inorder 分成两边进行递归处理
  - Valid Palindrome
  - Count and Say
  - Palindrome Number
   - 取第一位数字和最后一位数字来比较
  - Longest Common Prefix
  - Add Two Numbers

#### MinStack
  - 用额外一个 list 来保存 min_item 的历史

#### part11
  - Convert Sorted List to Binary Search Tree
   - 每一次把 list 分成两半来处理
