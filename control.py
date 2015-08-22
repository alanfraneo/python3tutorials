
x = 13

if x < 0:
    print("x is negative")
else:
    print("x is a positive number")


if x < 0:
    print("x is negative")
elif x >= 1 and x <= 9:
    print("x is a single digit number")
else:
    print("x is a positive number greater than 10")



if x < 0:
    print("x is negative")
elif x == 0:
    print("x is zero")
elif x >= 1 and x <= 9:
    print("x is a single digit number")
elif 10 <= x <= 19:
    print("x is in it's teens")
else:
    print("x is a positive number greater than 20")


eggs = ["good egg", "bad egg", "quail egg", "ostritch egg"]
if "good egg" in eggs:
    print("yes")

if "good egg" not in eggs:
    print("No good eggs")
