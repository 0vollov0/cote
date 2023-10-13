import random
import sorts

arr = [random.randint(10, 99) for _ in range(random.randint(1, 10))]

print('Generated List: ', arr)

sorts.quick_sort(arr)
print('Sorted List', sorts.quick_sort(arr))
