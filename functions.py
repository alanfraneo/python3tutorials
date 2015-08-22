

def printHi():  # parameterless function.
    print("Hi!")

printHi()


def printHiName(name):  # parameterized function, how about we say Hi using a name.
    print("Hi", name)

printHiName("Alan")


def add(var1, var2):  # function with a return value, how about a adding 2 values?
    return var1+var2

print("Add 2 and 5: ", add(2, 5))

print("Samething but called using named parameters:", add(var1=2, var2=5))

add(var2=5, var1=2)


def printHello(name="Stranger"):
    print("Hello ", name)

printHello("Alan")

printHello()

# functions with variable parameters:


def hellotoMany(name1, *args):
    print("Hello", name1)
    for eachname in args:
        print("hello ", eachname)

hellotoMany("Alan", "Jack", "Arya", "Jon")


def hellotoManyMore(name1, **kwargs):
    print("Hello", name1)
    print("Hello", kwargs.get('name2'))
    print("Hello", kwargs.get('name3'))

hellotoManyMore("Alan", name3="Jack", name2="Jon")


# A much more thought out example which explains other uses of keyword arguments or kwargs


def doSomething(first, second, third, **kwargs):
    if kwargs.get("action") == "sum":
        print("The sum is: %d" % (first + second + third))

    if kwargs.get("number") == "second":
        return second

result = doSomething(1, 2, 3, number="second")
print("1. Result: %d" % result)
result = doSomething(1, 2, 3, action="sum", number="second")
print("2. Result: %d" % result)
