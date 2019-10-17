# task nr 2.9

# task nr 2.10

# task nr 2.11
word = input("enter some word: ")
if len(word) > 0:
    for character in range(0, len(word) - 1):
        print(word[character], end='_')
    print(word[len(word) - 1])

# task nr 2.12
line = input("enter line: ")

first_letters = ''
last_letters = ''
words = []
words_sum = 0

if len(line) > 0:
    words = line.split()
for single_word in words:
    words_sum += len(single_word)
    first_letters += single_word[0]
    last_letters += single_word[len(single_word) - 1]
print("first letters word: %s, last letters word: %s" % (first_letters, last_letters))

# task nr 2.13

print("words sum is %d " % words_sum)

# task nr 2.14
# task nr 2.15
# task nr 2.16
# task nr 2.17
# task nr 2.18
# task nr 2.19
