import random as rd
import numpy as np


def array_of_numbers(n):
    numbers = []
    for i in range(n):
        numbers.append(i)
    return numbers


def random_unsorted_array(n):
    numbers = array_of_numbers(n)
    random_data = []

    while n > 0:
        index = rd.randint(0, n - 1)
        random_data.append(numbers[index])
        del numbers[index]
        n -= 1
    return random_data


def almost_sorted_array(n):
    unsorted_arr = random_unsorted_array(n)
    # sort with bubble sort some part of the unsorted array, in this way we have almost sorted array
    part_len = n - n // 4
    for i in range(part_len):
        for j in range(0, part_len - i - 1):
            if unsorted_arr[j] > unsorted_arr[j + 1]:
                unsorted_arr[j], unsorted_arr[j + 1] = unsorted_arr[j + 1], unsorted_arr[j]
    return unsorted_arr


def reversed_almost_sorted_array(n):
    return list(reversed(almost_sorted_array(n)))


def random_gaussian_dist_numbers_array(n):
    return list(np.random.randn(n))


def random_array_from_k_set(n):
    k_set = random_unsorted_array(rd.randint(1, n - 1))
    random_k_data = []

    for i in range(n):
        random_k_data.append(k_set[rd.randint(0, len(k_set) - 1)])
    return random_k_data


# (a) różne liczby int od 0 do N-1 w kolejności losowej,
# (b) różne liczby int od 0 do N-1 prawie posortowane (liczby są blisko swojej prawidłowej pozycji),
# (c) różne liczby int od 0 do N-1 prawie posortowane w odwrotnej kolejności,
# (d) N liczb float w kolejności losowej o rozkładzie gaussowskim,
# (e) N liczb int w kolejności losowej, o wartościach powtarzających się, należących do zbioru k elementowego
# (k < N, np. k*k = N).

if __name__ == "__main__":
    print(random_unsorted_array(15))
    print(almost_sorted_array(15))
    print(reversed_almost_sorted_array(15))
    print(random_gaussian_dist_numbers_array(15))
    print(random_array_from_k_set(15))

