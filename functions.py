import random
import statistics

#
# ENTRY POINT FOR QUICKSORT
#
def quickSort():
    print("QUICKSORT\n------\n")
    # initial setup
    integers = []
    output = ""
    global comparisons
    comparisons = 0

    # loop through all three txt files
    with open('qs_one.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                integers.append(int(line))

    sort(integers.copy())
    output += "Ten Integers:\n---\nComparisons with first element partition: " + str(comparisons) + '\n'
    comparisons = 0
    sort(integers.copy(), pivot_type="last")
    output += "Partition with last element: " + str(comparisons) + '\n'
    comparisons = 0
    sort(integers.copy(), pivot_type="median-of-three")
    output += "Partition with median-of-three: " + str(comparisons) + '\n'
    comparisons = 0
    sort(integers.copy(), pivot_type="random")
    output += "Partition with random element: " + str(comparisons) + '\n'

    integers = []
    with open('qs_two.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                integers.append(int(line))

    comparisons = 0
    sort(integers.copy())
    output += "\nOne Hundred Integers:\n---\nComparisons with first element partition: " + str(comparisons) + '\n'
    comparisons = 0
    sort(integers.copy(), pivot_type="last")
    output += "Partition with last element: " + str(comparisons) + '\n'
    comparisons = 0
    sort(integers.copy(), pivot_type="median-of-three")
    output += "Partition with median-of-three: " + str(comparisons) + '\n'
    comparisons = 0
    sort(integers.copy(), pivot_type="random")
    output += "Partition with random element: " + str(comparisons) + '\n'

    integers = []
    with open('qs_three.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                integers.append(int(line))
    
    comparisons = 0
    sort(integers.copy())
    output += "\nTen Thousand Integers:\n---\nComparisons with first element partition: " + str(comparisons) + '\n'
    comparisons = 0
    sort(integers.copy(), pivot_type="last")
    output += "Partition with last element: " + str(comparisons) + '\n'
    comparisons = 0
    sort(integers.copy(), pivot_type="median-of-three")
    output += "Partition with median-of-three: " + str(comparisons) + '\n'
    comparisons = 0
    sort(integers.copy(), pivot_type="random")
    output += "Partition with random element: " + str(comparisons) + '\n'

    return output

def _quickSort(arr, begin, length, pivot_type="first"):
    global comparisons
    if length <= 1:
        return 0

    if pivot_type == "last":
        arr[begin], arr[begin + length - 1] = arr[begin + length - 1], arr[begin]
    elif pivot_type == "median-of-three":
        first = arr[begin]
        last = arr[begin + length - 1]
        middle = arr[begin + (length - 1) // 2]
        pivot_value = statistics.median([first, middle, last])
        if pivot_value == first:
            pivot = begin
        elif pivot_value == middle:
            pivot = begin + (length - 1) // 2
        else:
            pivot = begin + length - 1
        arr[begin], arr[pivot] = arr[pivot], arr[begin]
    elif pivot_type == "random":
        pivot = random.randint(begin, begin + length - 1)
        arr[begin], arr[pivot] = arr[pivot], arr[begin]

    i = begin
    for j in range(begin + 1, begin + length):
        comparisons += 1
        if arr[j] < arr[begin]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[begin], arr[i] = arr[i], arr[begin]

    cmp_left = _quickSort(arr, begin, i - begin, pivot_type)
    cmp_right = _quickSort(arr, i + 1, begin + length - i - 1, pivot_type)

    return cmp_left + cmp_right + length - 1

def sort(arr, pivot_type="first"):
    _quickSort(arr, 0, len(arr), pivot_type)

#
# ENTRY POINT FOR LINEAR TIME SELECTION
#
def linearTimeSelection():
    return "Linear Time Selection"