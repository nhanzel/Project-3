from functions import quickSort, linearTimeSelection

# QS_ONE should count 25 comparisons if you always use the first element as the pivot,
# 31 comparisons if you always use the last element as the pivot,
# and 21 comparisons if you always use the median-of-3 as the pivot
# (not counting the comparisons used to compute the pivot).

# QS_TWO should count 620 comparisons if you always use the first element as the pivot,
# 573 comparisons if you always use the last element as the pivot,
# and 502 comparisons if you always use the median-of-3 as the pivot
# (not counting the comparisons used to compute the pivot).

# QS_THREE contains all of the integers between 1 and 10,000 (inclusive) in some order,
# with no integer repeated. The ith row of the file indicates the ith entry of an array.
# How many comparisons does QuickSort make on this input when the first element is always chosen as the pivot? 
# If the last element is always chosen as the pivot? If the median-of-3 is always chosen as the pivot? 
print(quickSort())

# QS_ONE What is the median (i.e., the 5th-smallest element)? (Solution: 5469.)

# QS_TWO What is the median (i.e., the 50th order statistic)? (Solution: 4715.)

# CHALLENGE: Form an array in which the first element is the first 10 digits of pi, 
# the second element is the next 10 digits of pi, and so on. (The digits of pi are available here.) 
# Make the array as big as you can (perhaps 100,000 elements, or 1 million elements, or ...). 
# What is the median of the array?
# Aside: do you think this array has any duplicate elements?

# BONUS CHALLENGE: Implement the deterministic linear-time selection algorithm from Section 6.3.
# For the challenge data set above, compare the maximum array lengths solvable in a reasonable amount of time 
# (e.g., one hour) with the randomized and deterministic linear-time selection algorithms. 
print(linearTimeSelection())