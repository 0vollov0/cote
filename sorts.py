def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        for j in range(i - 1, -1, -1):
            if arr[j + 1] < arr[j]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - (i + 1)):
            if arr[j + 1] < arr[j]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]


def merge_sort(arr, begin, end):
    center = (begin + end) // 2
    if center == begin:
        if arr[end] < arr[begin]:
            arr[begin], arr[end] = arr[end], arr[begin]
        return
    merge_sort(arr, begin, center)
    merge_sort(arr, center + 1, end)
    for i in range(begin, end + 1):
        for j in range(center + 1, end + 1):
            if (i < j and arr[i] > arr[j]) or (i > j and arr[i] < arr[j]):
                arr[i], arr[j] = arr[j], arr[i]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # 중앙 값을 피벗으로 선택
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
