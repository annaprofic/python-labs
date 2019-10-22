# TASK 3.1

# 1)
# x = 2 ; y = 3 ;
# if (x > y):
#     result = x;
# else:
#     result = y;

# 1) YES, but better without ' ; '


# 2) for i in "qwerty": if ord(i) < 100: print i
# 2) NO

for i in "qwerty":
    if ord(i) < 100:
        print(i)

# 3) for i in "axby": print ord(i) if ord(i) < 100 else i
# 3) NO

for i in "axby":
    print(i)

# TASK 3.2

# L = [3, 5, 4] ; L = L.sort()
# 1) the same line
# 2) with ' ; '
# 3) sort() function doesn't return anything
L = [3, 5, 4]
L.sort()

# x, y = 1, 2, 3
# to much values (3) for only two variables
x, y = 1, 2

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
for i in range(30):
    if i % 3:
        print(i, end=" ")

# TASK 3.4
length = int(input("Enter a length for task 3.4: "))

if length >= 10:
    length_add = 10 - length

ruler = ""

