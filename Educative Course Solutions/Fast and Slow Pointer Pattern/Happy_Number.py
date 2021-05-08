"""
Any number will be called a happy number if, after repeatedly replacing it with a number equal to the sum of the square of all of its digits, leads us to number ‘1’. All other (not-happy) numbers will never reach ‘1’. Instead, they will be stuck in a cycle of numbers which does not include ‘1’.

Example 1:

Input: 23   
Output: true (23 is a happy number)  
Explanations: Here are the steps to find out that 23 is a happy number:

Example 2:

Input: 12   
Output: false (12 is not a happy number)  
"""

"""

#Without two pointer
def find_happy_number(num):
  data = set()
  while True :
    data.add(num)
    num = findSquare(num)
    if num == 1 :
      return True
    elif num in data :
      break
  return False

#with two pointer (fast and slow)
def find_happy_number2(num) :
  i,j = num,num
  while True :
    i = findSquare(i) 
    j = findSquare(findSquare(j))
    if i==j :
      break
  return i == 1


def findSquare(num) :
  count = 0
  while num > 0 :
    i = num % 10
    count += i * i
    num  //= 10
  return count

def main():
  print(find_happy_number(23))
  print(find_happy_number(12))
  print(find_happy_number2(23))
  print(find_happy_number2(12))

main()
