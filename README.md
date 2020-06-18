# lintcode算法题

## 627
### 最长回文串
#### 描述

给出一个包含大小写字母的字符串。求出由这些字母构成的最长的回文串的长度是多少。

数据是大小写敏感的，也就是说，"Aa" 并不会被认为是一个回文串。

假设字符串的长度不会超过 100000。

样例

    样例 1:

    输入 : s = "abccccdd" 
    输出 : 7
    说明 : 
    一种可以构建出来的最长回文串方案是 "dccaccd"。
    
## 13
### 字符串查找
#### 描述

对于一个给定的 source 字符串和一个 target 字符串，你应该在 source 字符串中找出 target 字符串出现的第一个位置(从0开始)。如果不存在，则返回 -1。
  
说明
在面试中我是否需要实现KMP算法？

不需要，当这种问题出现在面试中时，面试官很可能只是想要测试一下你的基础应用能力。当然你需要先跟面试官确认清楚要怎么实现这个题。

样例
样例 1:

输入: source = "source" ， target = "target"
输出:-1	
样例解释: 如果source里没有包含target的内容，返回-1
样例 2:

输入: source = "abcdabcdefg" ，target = "bcd"
输出: 1	
样例解释: 如果source里包含target的内容，返回target在source里第一次出现的位置
挑战
O(n2)的算法是可以接受的。如果你能用O(n)的算法做出来那更加好。（提示：KMP）

## 415
### 有效回文
#### 描述
给定一个字符串，判断其是否为一个回文串。只考虑字母和数字，忽略大小写。

样例
样例 1:

    输入: "A man, a plan, a canal: Panama"
    输出: true
    解释: "amanaplanacanalpanama"
样例 2:

    输入: "race a car"
    输出: false
    解释: "raceacar"
挑战
    
    O(n) 时间复杂度，且不占用额外空间
    

### 200
#### 最长回文
##### 描述

给出一个字符串（假设长度最长为1000），求出它的最长回文子串，你可以假定只有一个满足条件的最长回文串

样例
样例 1:

    输入:"abcdzdcab"
    输出:"cdzdc"
    样例 2:

    输入:"aba"
    输出:"aba"

挑战
O(n2) 时间复杂度的算法是可以接受的，如果你能用 O(n) 的算法那自然更好。