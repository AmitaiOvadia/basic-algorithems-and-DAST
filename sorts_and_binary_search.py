
import numpy as np
import time
from MaxHeap import MaxHeap

def binary_search_recursive_split(nums, target):
    n = len(nums)
    middle = n//2
    if n == 1:
        if nums[0] == target:
            return True
        else:
            return False
    if target == nums[middle]:
        return True
    if target < nums[middle]:
        return binary_search_recursive_split(nums[:middle], target)
    else:
        return binary_search_recursive_split(nums[middle:], target)


def binary_search_recursive_indexing(nums, target, L, R):
    if L == R:
        if nums[L] == target:
            return True
        else:
            return False
    n = len(nums)
    middle = (L + R + 1) // 2
    if nums[middle] == target:
        return True
    if target > nums[middle]:
        return binary_search_recursive_indexing(nums, target, middle + 1, R)
    else:
        return binary_search_recursive_indexing(nums, target, L, middle - 1)


def binary_search_iterative(nums, target):
    L = 0
    R = len(nums) - 1
    while L != R:
        middle = (L + R + 1)//2
        if nums[middle] == target:
            return True
        if target < nums[middle]:
            R = middle - 1
            continue
        else:
            L = middle + 1
            continue
    if nums[L] == target:
        return True
    return False


# sorts:
def bubble_sort(A):
    # starts from begining of array: if A[i] > A[i + 1] : switch
    n = len(A)
    for i in range(n):
        for j in range(n - i - 1):
            if A[j] > A[j + 1]:
                A[j + 1], A[j] = A[j], A[j + 1]
    return A


def merge(A,B):
    # merges 2 sorted array into 1 sortet array

    C = np.zeros(len(A) + len(B))
    n = len(C)
    c, a, b = 0, 0, 0
    while a < len(A) and b < len(B):
        if A[a] < B[b]:
            C[c] = A[a]
            a += 1
        else:
            C[c] = B[b]
            b += 1
        c += 1
    if a < len(A):  # B is done
         while a < len(A):
             C[c] = A[a]
             a += 1
             c += 1

    if b < len(B):  # B is done
        while b < len(B):
            C[c] = B[b]
            b += 1
            c += 1
    return C

def merge_sort_recursive(A):
    n = len(A)
    if n <= 1:
        return A
    R = merge_sort_recursive(A[:n//2])
    L = merge_sort_recursive(A[n//2:])
    return merge(L, R)


def merge_sort_iterative(A):
    pass


def partition(A, L, R):
    # takes the rightmost element (pivot) and returns the array such that
    # the pivot is in its rightful place in a sorted array:
    # all the smaller numbers are on the right, and bigger are on the left
    pivot = A[R]
    i = L - 1  # represents the rightmost location the pivot had found for itself so far
    for j in range(L, R):
        if A[j] <= pivot:
            i += 1
            A[j], A[i] = A[i], A[j]  # swap
    A[i + 1], A[R] = A[R], A[i + 1]
    return i + 1


def quick_sort_recursive(A, L, R):
    if L < R:
        pivot = partition(A, L, R)
        quick_sort_recursive(A, L, pivot - 1)
        quick_sort_recursive(A, pivot + 1, R)


def countSort(arr):
    k = np.max(arr)
    count = np.zeros(k + 1)
    for i in arr:
        count[i] += 1
    output = np.zeros(len(arr))
    k = 0
    for i, val in enumerate(count):
        for j in range(int(val)):
            output[k] = i
            k += 1
    return output


def quik_sort_iterative(A):
    pass


def check_sort_runtime():
    iterations = 100
    array_len = 10000
    array_max = 1000

    start_time = time.time()
    for i in range(iterations):
        A = np.random.randint(0, array_max, (array_len,))
        A = MaxHeap.heap_sort(A)
    print("MaxHeap.heap_sort took ", time.time() - start_time)

    start_time = time.time()
    for i in range(iterations):
        A = np.random.randint(0, array_max, (array_len,))
        A = countSort(A)
    print("countSort took ", time.time() - start_time)

    start_time = time.time()
    for i in range(iterations):
        A = np.random.randint(0, array_max, (array_len,))
        quick_sort_recursive(A, 0, len(A) - 1)
    print("quick sort took ", time.time() - start_time)

    start_time = time.time()
    for i in range(iterations):
        A = np.random.randint(0, array_max, (array_len,))
        A = merge_sort_recursive(A)
    print("merge_sort took ", time.time() - start_time)

    start_time = time.time()
    for i in range(iterations):
        A = np.random.randint(0, array_max, (array_len,))
        A = np.sort(A)
    print("numpy sort took ", time.time() - start_time)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    check_sort_runtime()

    # A = merge_sort_recursive(A)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
