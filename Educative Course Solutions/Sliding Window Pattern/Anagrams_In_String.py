"""
Given a string and a pattern, find all anagrams of the pattern in the given string.
Anagram is actually a Permutation of a string. For example, “abc” has the following six anagrams:

abc
acb
bac
bca
cab
cba
Write a function to return a list of starting indices of the anagrams of the pattern in the given string.

Input: String="ppqp", Pattern="pq"
Output: [1, 2]
Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".

Input: String="abbcabc", Pattern="abc"
Output: [2, 3, 4]
Explanation: The three anagrams of the pattern in the given string are "bca", "cab", and "abc".

"""
def find_string_anagrams(str, pattern):
  result_indexes = []
  start = 0
  freq = {s : pattern.count(s) for s in pattern}
  matched = 0
  for end in range(len(str)) :
    c = str[end]
    if c in freq :
      freq[c] -= 1
      if freq[c] == 0 :
        matched += 1
    
    if matched == len(freq) :
      result_indexes.append(start)

    if end >= len(pattern) -1:
      c = str[start]
      start += 1
      if c in freq : 
        if freq[c] == 0 :
          matched -= 1
        freq[c] += 1 

  return result_indexes

