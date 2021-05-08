"""
Given a list of non-overlapping intervals sorted by their start time, insert a given interval at the correct position and merge all necessary intervals to produce a list that has only mutually exclusive intervals.

Example 1:

Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,6]
Output: [[1,3], [4,7], [8,12]]
Explanation: After insertion, since [4,6] overlaps with [5,7], we merged them into one [4,7].
Example 2:

Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,10]
Output: [[1,3], [4,12]]
Explanation: After insertion, since [4,10] overlaps with [5,7] & [8,12], we merged them into [4,12].
Example 3:

Input: Intervals=[[2,3],[5,7]], New Interval=[1,4]
Output: [[1,4], [5,7]]
Explanation: After insertion, since [1,4] overlaps with [2,3], we merged them into one [1,4].

"""


def insert(intervals, new_interval):
  merged = []
  interval = new_interval
  flag = False
  for i in range(len(intervals)) :
    if checkOverlap(interval, intervals[i]) :
      interval = merge(interval,intervals[i])
    else:
      if interval[0] < intervals[i][0] :
        merged.append(interval)
        flag = True
      merged.append(intervals[i])

  if not flag :
    merged.append(interval)
  return merged

def checkOverlap(i1,i2) :
  if i1[0] > i2[1] or i2[0] > i1[1] :
    return False
  return True

def merge(i1,i2) :
  return [min(i1[0], i2[0]), max(i1[1], i2[1])]

def main():
  print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 6])))
  print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 10])))
  print("Intervals after inserting the new interval: " + str(insert([[2, 3], [5, 7]], [1, 4])))


main()
