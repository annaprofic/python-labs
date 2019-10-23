# -------TASK 3.1--------

# 1)
# x = 2 ; y = 3 ;
# if (x > y):
#     result = x;
# else:
#     result = y;

# 1) YES, but better without ' ; '


# 2) for i in "qwerty": if ord(i) < 100: print i
# 2) NO
# prepare way to loop:
# for i in "qwerty":
#     if ord(i) < 100:
#         print(i)

# 3) for i in "axby": print ord(i) if ord(i) < 100 else i
# 3) NO
# prepare way to loop:
# for i in "axby":
#     print(i)

# -------TASK 3.2----------

# L = [3, 5, 4] ; L = L.sort()
# 1) the same line
# 2) with ' ; '
# 3) sort() function doesn't return anything

# prepare way to sort list:
# L = [3, 5, 4]
# L.sort()

# x, y = 1, 2, 3
# to much values (3) for only two variables
# prepare way to initialize variables:
# x, y = 1, 2

# X = 1, 2, 3 ; X[1] = 4
# tuples are immutable


# X = [1, 2, 3] ; X[3] = 4
# array hasn't third-index item
# it's has only 0, 1, 2 indexes

# X = "abc" ; X.append("d")
# append function is for list

# map(pow, range(8))
# pow function expect 2 arguments instead of 1


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

