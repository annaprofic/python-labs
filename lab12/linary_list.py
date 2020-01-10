import random as rd


def gen_random_list(k, n=100):
    temp_l = []
    for i in range(n):
        temp_l.append(rd.randint(0, k - 1))
    return temp_l


def find_all_occurrences(k=10):

    elements = gen_random_list(k)
    seeked = rd.randint(0, k - 1)
    occurrences = 0

    print(f"\ngenerated list: {elements}.")
    print(f"\nsearching for '{seeked}' element...\n")

    for index, current_val in enumerate(elements):
        if current_val == seeked:
            print(f"found on index: {index}")
            occurrences += 1

    print(f"\n{occurrences} occurrences of '{seeked}' found.")


find_all_occurrences()
