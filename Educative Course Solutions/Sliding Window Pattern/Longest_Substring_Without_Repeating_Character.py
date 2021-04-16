#Given a string, find the length of the longest substring, which has no repeating characters.

def non_repeat_substring(str):
  count=0
  start=0
  for end in range(len(str)) :
    u = unique(str[start : end])
    if len(str[start:end]) == u :
      count = max(count, end-start)
    while len(str[start:end]) != u :
      start += 1
      u = unique(str[start : end])
      count = max(count, end-start)

  return count

def unique(str) :
  return len(set(str))