# TASK 3.4


def is_float(inp):
    try:
        float(inp)
        return True
    except ValueError:
        return False


continue_input = True

print("\n\nEnter 'stop' keyword to stop program")

while continue_input:
    user_in = input("\nEnter float number to continue: ")

    if user_in == "stop":
        continue_input = False

    elif is_float(user_in):
        print(user_in, pow(float(user_in), 3))

    else:
        print("Error: wrong argument format")
