
num1 = 10

def addToNum(num2):
    global num1
    num1 += 20
    print(num1+num2)

addToNum(12)
print("num1: ", num1)


def addToNumber(num2):
    gnum1 = num1  # gnum1 is a local variable
    print(gnum1+num2)
    return gnum1

x = addToNumber(12)
print("num1: ", x)
