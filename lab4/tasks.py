# # TASK 4.2 (from 3.5)
# def draw_ruler(length):
#     if length < 1 or length > 30:
#         raise Exception("Number from task 3.5 must be from 1 to 30.")
#
#     ruler = "|"
#     numbers = "1"
#
#     for i in range(1, length):
#         ruler += "...|"
#         if i < 9:
#             numbers += "   " + str(i + 1)
#         else:
#             numbers += "  " + str(i + 1)
#
#     print("TASK 3.5 result: ")
#     return ruler + "\n" + numbers
#
#
# # TASK 4.2 (from 3.6)
# def draw_rectangle(inp):
#     n, m = 0, 0
#
#     try:
#         n = int(inp[0])
#         m = int(inp[1])
#     except ValueError:
#         print("Wrong agrs for task 3.6.")
#
#     horizontal_line = "+"
#     vertical_line = "|"
#     rectangle = ""
#
#     for i in range(0, m):
#         horizontal_line += "---+"
#         vertical_line += "   |"
#
#     return rectangle + (horizontal_line + "\n" + vertical_line + "\n") * n + horizontal_line
#
#
# # TASK 4.3
# def factorial_rec(n):
#     if n == 1:
#         return n
#     return n * factorial_rec(n - 1)
#
#
# def factorial_iter(n):
#     fact = 1
#
#     for i in range(1, n + 1):
#         fact *= i
#     return fact
#
#
# # TASK 4.4
# def fibonacci_rec(n2):
#     if n2 == 0:
#         return 0
#     if n2 == 1:
#         return 1
#     return fibonacci_rec(n2 - 1) + fibonacci_rec(n2 - 2)
#
#
# def fibonacci_iter(n2):
#     a, b = 0, 1
#     if n2 == 0:
#         return a
#     if n2 == 1:
#         return b
#     for i in range(2, n2 + 1):
#         c = a + b
#         a = b
#         b = c
#     return b


# TASK 4.5
def reverse_rec(t_list, left, right):
    t_list[right], t_list[left] = t_list[left], t_list[right]
    if not (int(right - left) == 1) and not (int(right - left) == 2):
        reverse_rec(t_list, left + 1, right - 1)
    return t_list


def reverse_iter(t_list, left, right):
    while not (int(right - left) == 1) and not (int(right - left) == 2):
        t_list[right], t_list[left] = t_list[left], t_list[right]
        left += 1
        right -= 1
    return t_list


# TASK 4.6
def sum_seq(sequence):
    sum_ = 0
    for i in sequence:
        if isinstance(i, (list, tuple)):
            sum_ += sum_seq(i)
        else:
            sum_ += i
    return sum_


# TASK 4.7

def flatten(sequence):
    temp_list = []
    for i in sequence:
        if isinstance(i, (list, tuple)):
            temp_list += flatten(i)
        else:
            temp_list.append(i)
    return temp_list


if __name__ == '__main__':
    # # 2
    # length = int(input("\nTASK 3.5 Enter a length for task 3.4 from 1 to 30: "))
    # print(draw_ruler(length))
    #
    # inp = input("\nTASK 3.5 Enter the rectangle size n x m: ").split()
    # print(draw_rectangle(inp))
    #
    # # 3
    # n = int(input("\nTASK 4.3 Enter some number 'n' and get n!: "))
    #
    # fac_a, fac_b = factorial_rec(n), factorial_iter(n)
    # assert fac_a == fac_b
    # print("TASK 4.3 result recursive: {0}, iterative: {1}".format(fac_a, fac_b))
    #
    # # 4
    # n2 = int(input("\nTASK 4.4 Enter some number 'n' and get Fibonacci number: "))
    #
    # fib_a, fib_b = fibonacci_rec(n2), fibonacci_iter(n2)
    # assert fib_a == fib_b
    # print("TASK 4.4 result recursive: {0}, iterative: {1}".format(fib_a, fib_b))

    # 5
    list_inp = input("\nTASK 4.5 Enter your list: ").split(" ")
    list_inp_copy = list(list_inp)
    left = int(input("reverse it from: ")) - 1
    right = int(input("to: ")) - 1

    rev_a, rev_b = reverse_rec(list_inp, left, right), reverse_iter(list_inp_copy, left, right)
    # assert rev_a == rev_b
    print("TASK 4.5 result recursive: {0}, \n\t\t\t\titerative: {1}".format(rev_a, rev_b))

    # 6
    print("\nTASK 4.6/7 example sequence is [1, (2, 3), [], [4, (5, 6, 7)])\n\nTASK 4.6 result",
          sum_seq([1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]))

    # 7
    print("TASK 4.7 result", flatten([1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]))
