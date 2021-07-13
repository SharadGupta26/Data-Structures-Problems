"""
Given a string, find all of its permutations preserving the character sequence but changing case.

Example 1:

Input: "ad52"
Output: "ad52", "Ad52", "aD52", "AD52" 
Example 2:

Input: "ab7c"
Output: "ab7c", "Ab7c", "aB7c", "AB7c", "ab7C", "Ab7C", "aB7C", "AB7C"
"""

from collections import deque
def find_letter_case_string_permutations(str):
  permutations = []
  elements= deque()
  elements.append('')
  for i in str :
    n = len(elements) 
    for _ in range(n) :
      s = elements.popleft()
      new = s + i.lower()
      if len(new) == len(str) :
        permutations.append(new)
      else :
        elements.append(new)
      if(i.isalpha()) :
        new = s + i.upper()
        if len(new) == len(str) :
          permutations.append(new)
        else :
          elements.append(new)
  return permutations


def main():
  print("String permutations are: " +
        str(find_letter_case_string_permutations("ad52")))
  print("String permutations are: " +
        str(find_letter_case_string_permutations("ab7c")))


main()
