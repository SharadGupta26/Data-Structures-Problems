"""
Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.

Example 1:

Intervals: [[1,4], [2,5], [7,9]]
Output: [[1,5], [7,9]]
Explanation: Since the first two intervals [1,4] and [2,5] overlap, we merged them into 
one [1,5].
svg viewer
Example 2:

Intervals: [[6,7], [2,4], [5,9]]
Output: [[2,4], [5,9]]
Explanation: Since the intervals [6,7] and [5,9] overlap, we merged them into one [5,9].

Example 3:

Intervals: [[1,4], [2,6], [3,5]]
Output: [[1,6]]
Explanation: Since all the given intervals overlap, we merged them into one.
"""

from __future__ import print_function


class Interval:
  def __init__(self, start, end):
    self.start = start
    self.end = end

  def print_interval(self):
    print("[" + str(self.start) + ", " + str(self.end) + "]", end='')



def merge(intervals):
  merged = []

  #Sorting to bring all overlapping intervals close to each other
  intervals.sort(key = lambda x : x.start)

  interval = intervals[0]
  for i in range(1,len(intervals)) :
    if checkoverlap(interval, intervals[i]) :
      interval = merge2Intervals(interval, intervals[i])
    else :
      merged.append(interval)
      interval = intervals[i]
  merged.append(interval)
  return merged

def checkoverlap(i1, i2) :
  if i1.end < i2.start or i2.end < i1.start :
    return False
  return True

def merge2Intervals(i1, i2) :
  return Interval(min(i1.start, i2.start), max(i1.end, i2.end))

  
def main():
  print("Merged intervals: ", end='')
  for i in merge([Interval(1, 4), Interval(2, 5), Interval(7, 9)]):
    i.print_interval()
  print()

  print("Merged intervals: ", end='')
  for i in merge([Interval(6, 7), Interval(2, 4), Interval(5, 9)]):
    i.print_interval()
  print()

  print("Merged intervals: ", end='')
  for i in merge([Interval(1, 4), Interval(2, 6), Interval(3, 5)]):
    i.print_interval()
  print()

main()