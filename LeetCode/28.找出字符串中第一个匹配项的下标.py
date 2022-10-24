'''
Author: water.li
Date: 2022-10-24 20:10:36
Description: 
FilePath: \note\LeetCode\28.找出字符串中第一个匹配项的下标.py
'''
#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 找出字符串中第一个匹配项的下标
#
# https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
#
# algorithms
# Medium (41.47%)
# Likes:    1622
# Dislikes: 0
# Total Accepted:    754.5K
# Total Submissions: 1.8M
# Testcase Example:  '"sadbutsad"\n"sad"'
#
# 给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串的第一个匹配项的下标（下标从 0
# 开始）。如果 needle 不是 haystack 的一部分，则返回  -1 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：haystack = "sadbutsad", needle = "sad"
# 输出：0
# 解释："sad" 在下标 0 和 6 处匹配。
# 第一个匹配项的下标是 0 ，所以返回 0 。
# 
# 
# 示例 2：
# 
# 
# 输入：haystack = "leetcode", needle = "leeto"
# 输出：-1
# 解释："leeto" 没有在 "leetcode" 中出现，所以返回 -1 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= haystack.length, needle.length <= 10^4
# haystack 和 needle 仅由小写英文字符组成
# 
# 
#

# @lc code=start
class Solution:
  def strStr(self, haystack: str, needle: str) -> int:
    if needle == '':
      return 0
    nexts = self.getNext(needle)
    hi, ne = 0, 0
    while hi < len(haystack):
      if ne == -1 or haystack[hi] == needle[ne]:
        if ne == len(needle) - 1: # 匹配成功
          return hi - len(needle) + 1
        hi += 1
        ne += 1
      else:
        ne = nexts[ne]
    return -1

  def getNext(self, needle: str):
    i, j, ret = 0, -1, [-1]
    while i < len(needle):
      if j == -1 or needle[i] == needle[j]:
        i += 1
        j += 1
        ret.insert(i, j)
      else:
        j = ret[j]
    return ret
      
# @lc code=end

