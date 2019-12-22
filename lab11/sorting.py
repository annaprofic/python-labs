# task 11.3
import lab11.data_sets as data


def cmp(x, y):
    if x > y:
        return 1
    if x == y:
        return 0
    return -1


def insertion_sort(arr, left, right, cmp_func=cmp):
    for i in range(left + 1, right + 1):
        item = arr[i]
        j = i
        while cmp_func(j, left) + cmp_func(arr[j-1], item) == 2:  # when both return 1
            arr[j] = arr[j-1]
            j = j - 1
        arr[j] = item
    return arr


if __name__ == "__main__":
    n = 15
    data_array = data.random_unsorted_array(n)
    print("random array: ", data_array)
    print("sorted: ", insertion_sort(data_array, 0, n - 1))

    data_array = data.almost_sorted_array(n)
    print("almost sorted array: ", data_array)
    print("sorted: ", insertion_sort(data_array, 0, n - 1))

    data_array = data.reversed_almost_sorted_array(n)
    print("reversed almost sorted array: ", data_array)
    print("sorted: ", insertion_sort(data_array, 0, n - 1))

    data_array = data.random_gaussian_dist_numbers_array(n)
    print("random gaussian dist numbers array: ", data_array)
    print("sorted: ", insertion_sort(data_array, 0, n - 1))

    data_array = data.random_array_from_k_set(n)
    print("random array from k set: ", data_array)
    print("sorted: ", insertion_sort(data_array, 0, n - 1))
