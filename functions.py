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
    print("LINEAR TIME SELECTION WITH DSELECT\n------\n")
    # initial setup
    integers = []
    output = ""

    # loop through all three txt files
    with open('qs_one.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                integers.append(int(line))

    result = dselect(integers, 5)
    output += "Ten Integers:\n---\n5th Element: " + str(result) + '\n'

    integers = []
    with open('qs_two.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                integers.append(int(line))

    result = dselect(integers, 50)
    output += "\nOne Hundred Integers:\n---\n50th Element: " + str(result) + '\n'

    integers = []
    with open('pi.txt', 'r') as file:
        elementCounter = 0
        currentNumber = ""
        while True:
            char = file.read(1)
            if not char:
                break
            if char.isdigit():
                currentNumber += char
                elementCounter += 1
                if elementCounter == 10:
                    integers.append(int(currentNumber))
                    currentNumber = ""
                    elementCounter = 0
    output += "\nPi Array:\n---\nMedian: " + str(dselect(integers, len(integers) // 2, return_median=True)) + '\n'
    return output

# DSelect Implementation
def dselect(arr, i, return_median=False):
    if len(arr) == 1:
        return arr[0]

    medians = []
    for j in range(0, len(arr), 5):
        group = arr[j:j + 5]
        medians.append(sorted(group)[len(group) // 2])  # Find the median of each group

    # Step 2: Find the median of medians
    if len(medians) <= 5:
        pivot = sorted(medians)[len(medians) // 2]
    else:
        pivot = dselect(medians, len(medians) // 2)

    if return_median:
        return pivot

    # Step 3: Partition array around pivot
    low = [x for x in arr if x < pivot]
    high = [x for x in arr if x > pivot]
    pivot_count = len(arr) - len(low) - len(high)  # Count occurrences of the pivot itself

    # Step 4: Determine which part of the array to search
    if i <= len(low):  # The i-th smallest is in the "low" part
        return dselect(low, i)
    elif i > len(low) + pivot_count:  # The i-th smallest is in the "high" part
        return dselect(high, i - len(low) - pivot_count)
    else:  # The pivot is the i-th smallest element
        return pivot