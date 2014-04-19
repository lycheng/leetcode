leetcode
========

leetcode AC codes

problems: http://oj.leetcode.com/problems/


#### reverseWords

提交了四次，第一次没有考虑到前导的空格问题，第二次没有考虑到中间的多余的空格。

第三次使用了 ```strip``` 之后再用 ```' '.join(s.split())``` 来清理多余的空格

第四次发现其实直接用 ```' '.join(s.split())``` 就好了


### singleNumber

a ^ b ^ a = b
