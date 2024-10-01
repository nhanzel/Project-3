from numpy import random
import sys
comparisons = 0

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    global comparisons
    comparisons += len(arr) - 1
    pivot = arr[random.randint(len(arr))] # random pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]  # Account for duplicate values
    right = [x for x in arr if x > pivot] 
    return quicksort(left) + middle + quicksort(right)

def quickselect(arr, k):
    if len(arr) == 1:
        return arr[0]
    global comparisons
    comparisons += len(arr) - 1
    pivot = arr[random.randint(len(arr))] # random pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]  # Account for duplicate values
    right = [x for x in arr if x > pivot]

    if k < len(left):
        return quickselect(left, k) # k-th smallest must be in left partition
    elif k < len(left) + len(middle):
        return middle[0]  # k-th smallest is the pivot
    else:
        return quickselect(right, k - len(left) - len(middle))  # k-th smallest is in the right partition

def main():
    # Read file
    if (len(sys.argv) != 3):
        print("Please provide exactly two CLI arguments: the filepath to the appropriate test file & the algorithm to use(sort or select).")
        exit()
    file_path = sys.argv[1]
    print(f"Opening {file_path}!")
    try:
        with open(file_path, 'r') as file:
            content = file.readlines()
            arr = [int(line.strip()) for line in content]  # Strip whitespace/newline characters and cast to integer
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
        exit()
    except IOError:
        print("An error occurred while reading the file.")
        exit()
    
    if (sys.argv[2] == "sort"):
        sorted = quicksort(arr)
        for it in sorted: # Debug
            print(it)
    elif (sys.argv[2] == "select"):
        _k = int(input("Quickselect to find the k-th smallest item. Enter k:"))
        res = quickselect(arr, _k)
        print(f"The {_k}th order item is {res}")
    else:
        print("CLI arguments not recognized...")
        exit()
    print("Number of comparisons:", comparisons)

if __name__ == "__main__":
    main()

