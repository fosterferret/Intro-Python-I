import math


# def main(sorted_collection, item):
#     left = 0
#     right = len(sorted_collection) - 1
#     while left <= right:
#         midpoint = left + (right - left) // 2
#         print(f'midpoint: {midpoint}, left: {left}, right: {right}')
#         current_item = sorted_collection[midpoint]
#         if current_item == item:
#             return True
#         elif item < current_item:
#             right = midpoint - 1
#         else:
#             left = midpoint + 1
#     return None


def main(sorted, item):
    left = 0
    right = len(sorted) - 1
    while left <= right:
        midpoint = left + (right - left) // 2
        curr = sorted[midpoint] 
        if curr == item:
            return True
        elif item < curr:
            right = midpoint - 1
        else:
            left = midpoint + 1
    return False


arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18]

print(main(arr, 12))
