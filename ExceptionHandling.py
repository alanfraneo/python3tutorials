# a = 1/0  # ZeroDivisionError

# b = x * 10  # NameError

# c = 'String' + 42  # TypeError


def printProductandQuotient(var1,var2):
    product = var1 * var2
    quotient = var1 / var2
    print("product of var1 and var2 is:", product)
    print("quotient when dividing",var1, "with", var2, "is:", quotient)

printProductandQuotient(10, 2)
# printProductandQuotient(10, 0)


def printProductandQuotientProper(var1, var2):
    """
    Sample program to showcase exception handling of a divide-by-zero error.
    """
    product = var1 * var2
    print("product of var1 and var2 is:", product)
    try:
        quotient = var1 / var2
        print("quotient when dividing", var1, "with", var2, "is:", quotient)
    except ZeroDivisionError:
        print("we cannot divide a number by 0, it results in infinity")

printProductandQuotientProper(10, 2)
printProductandQuotientProper(10, 0)


def testFinally():
    """
    Sample program to showcase the finally block.
    """
    try:
        x = 1/0
    except TypeError:
        print("there was a type error in the code")
    finally:
        print("some other exception occurred, gracefully shutting down")
        ''' do something here to gracefully shutdown app'''

testFinally()
