#Given a string, find the length of the longest substring in it with no more than K distinct characters.

def longest_substring_with_k_distinct(str, k):
  start = 0
  l = 0
  for end in range(len(str)) :
    l = max(l, end-start)
    while distinct(str[start:end+1]) > k :
      start += 1
      l = max(l, end-start)
  return l

def distinct(str) :
  return len(set(str))
