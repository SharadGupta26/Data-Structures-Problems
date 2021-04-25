"""
Given a string and a pattern, find the smallest substring in the given string which has all the characters of the given pattern.

Example 1:

Input: String="aabdec", Pattern="abc"
Output: "abdec"
Explanation: The smallest substring having all characters of the pattern is "abdec"
Example 2:

Input: String="abdbca", Pattern="abc"
Output: "bca"
Explanation: The smallest substring having all characters of the pattern is "bca".
Example 3:

Input: String="adcad", Pattern="abc"
Output: ""
Explanation: No substring in the given string has all characters of the pattern.    
"""

def find_substring(str, pattern):
  freq = { s : pattern.count(s) for s in pattern}
  start = 0
  matched = 0
  res = str
  for end in range(len(str)) :
    c = str[end]
    if c in freq :
      freq[c] -= 1
      if freq[c] == 0 :
        matched += 1
    
    if matched == len(freq) : 
      res = res if len(res) < end-start + 1 else str[start:end + 1]
    while matched == len(freq) :
      c = str[start]
      res = res if len(res) < end-start + 1 else str[start:end + 1]
      start += 1
      
      if c in freq :
        if freq[c] == 0 :
          matched -=1
        freq[c] += 1
  return "" if res == str and matched < len(pattern) else res
