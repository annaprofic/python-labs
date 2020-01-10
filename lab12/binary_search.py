def binary_rec(arr, left, right, y):

    if left > right:
        return None

    mid = left + right // 2

    if arr[mid] == y:
        return mid
    if arr[mid] > y:
        return binary_rec(arr, left, mid - 1, y)
    return binary_rec(arr, mid + 1, right, y)


test_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
test_list3 = [1, 2, 3, 4]
test_list4 = [1, 2]

assert binary_rec(test_list1, 0, len(test_list1) - 1, 6) == 5
assert binary_rec(test_list1, 0, len(test_list1) - 1, 2) == 1
assert binary_rec(test_list1, 0, len(test_list1) - 1, 15) == 14

assert binary_rec(test_list3, 0, len(test_list3) - 1, 5) is None
assert binary_rec(test_list4, 0, len(test_list4) - 1, 3) is None
