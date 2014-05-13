leetcode
========

leetcode AC codes

problems: http://oj.leetcode.com/problems/

#### part1

### reverseWords

提交了四次，第一次没有考虑到前导的空格问题，第二次没有考虑到中间的多余的空格。

第三次使用了 ```strip``` 之后再用 ```' '.join(s.split())``` 来清理多余的空格

第四次发现其实直接用 ```' '.join(s.split())``` 就好了

### singleNumber

a ^ b ^ a = b

### maxDepth

DFS

### isSameTree

DFS

### reverse number

这道题用 python 略犯规啊，它好心提示一点用都没有

### hasCycle

前面一个指针一次跳两个，后面一个指针一次跳一个，总会相遇

### preorder && inorder

### searchInsert

### deleteDuplicates

### climbStairs

第一次用递归做超时，后面想了下，大概的思路是：到达某一个 n 可能的步数就是到达 n - 1 和到达 n - 2 的和
