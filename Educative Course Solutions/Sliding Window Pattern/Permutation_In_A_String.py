#Given a string and a pattern, find out if the string contains any permutation of the pattern.

#Permutation is defined as the re-arranging of the characters of the string. For example, “abc” has the following six permutations:

#abc
#acb
#bac
#bca
#cab
#cba
#If a string has ‘n’ distinct characters, it will have n! permutations.


def find_permutation(str, pattern):
  data = {s : pattern.count(s) for s in pattern}
  start=0
  for end in range(len(str)) :
    if str[end] not in data :
      start = end + 1
    if end - start + 1 == len(data) :
      return True
  return False
