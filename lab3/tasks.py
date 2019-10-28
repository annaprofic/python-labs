# TASK 3.3
print("\nTASK 3.3 result: ", end="")
for i in range(30):
    if i % 3:
        print(i, end=" ")

# TASK 3.4

print("\n\nTASK 3.4 Enter 'stop' keyword to stop the task.")

while True:
    user_in = input("Enter float number to continue: ")

    if user_in == "stop":
        break

    try:
        float(user_in)
        print(user_in, pow(float(user_in), 3))
    except ValueError:
        print("Error: wrong argument format")

# TASK 3.5

length = int(input("\nTASK 3.5 Enter a length for task 3.4 from 1 to 30: "))

if length < 1 or length > 30:
    raise Exception("Number from task 3.5 must be from 1 to 30.")

ruler = "|"
numbers = "1"

for i in range(1, length):
    ruler += "...|"
    if i < 9:
        numbers += "   " + str(i + 1)
    else:
        numbers += "  " + str(i + 1)

ruler += "\n" + numbers
print("TASK 3.5 result: ")
print(ruler)

# TASK 3.6
inp = input("\nTASK 3.5 Enter the rectangle size n x m: ").split()
n, m = 0, 0

try:
    n = int(inp[0])
    m = int(inp[1])
except ValueError:
    print("Wrong agrs for task 3.6.")

horizontal_line = "+"
vertical_line = "|"
rectangle = ""

# for i in range(2):
for i in range(0, m):
    horizontal_line += "---+"
    vertical_line += "   |"

rectangle += (horizontal_line + "\n" + vertical_line + "\n") * n + horizontal_line

print(rectangle)

# TASK 3.8
list1 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 2, 8, 9]
list2 = [1, 2, 10, 12, 11, -1, 0, 2, 3, 4, 15]
print("\nTASK 3.8 example list1: {0} \n\t\t example list2: {1}".format(list1, list2))

print("\n1. The common elements of two lists without duplicates: ", set(list1) & set(list2))
print("2. All elements from two lists without duplicates:", set(list1 + list2))

# TASK 3.9
list_of_lists = [[], [4], (1, 2), [3, 4], (5, 6, 7)]
print("\nTASK 3.9 example list from task description: {0}".format(list_of_lists))
print("TASK 3.9 result", list(map(lambda x: sum(x), list_of_lists)))


# TASK 3.10
roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def roman2int(number):
    return roman.get(number)


def roman2int2(number):
    answer = 0
    pre_num = 0
    for c in number:
        answer += roman[c]
        if roman[c] > pre_num:
            answer -= pre_num * 2
        pre_num = roman[c]
    return answer


number1 = input("\nTASK 3.10 Enter roman simple number: ")
print("-> ", roman2int(number1))
number2 = input("\nTASK 3.10 Enter roman number from 1 to 3999: ")
print("-> ", roman2int2(number2))







