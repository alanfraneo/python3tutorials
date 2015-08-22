
# ways to initiate a tuple
tupleExample = 5, 6, 2, 6
tupleExample1 = (5, 6, 7, 8)

print("Tuple  ", tupleExample)
# accessing a tuple's element
print("Second element of tupleExample ", tupleExample[1])

# ways to create a list, use square brackets
listExample = [5, 2, 4, 1]

print("List:", listExample)
# accessing a List's element
print("Third element of list:", listExample[2])

# slicing of data is to get a subset of the list as another list, by providing a range for the index
print("a slice of the data:", listExample[1:4])  # brings up 1, 2 and 3rd element

# we can access the list from the end, using negative index values.
# The last index value is -1 and the last but one is -2 so on and so forth
print("The last element in this list:", listExample[-1])
print("The last but second element in this list:", listExample[-2])


listExample = [5, 2, 4, 1]
print("List:", listExample)
listExample.append(2)
print("2 added to the end of the List:", listExample)

listExample.insert(2, 77)
print("77 inserted at 3rd location in the List:", listExample)

listExample.remove(2)  # will remove the first occuring 2 in the list
print("value 2 is removed from the list:", listExample)

listExample.remove(listExample[1])  # will remove the 2nd element of the list
print("2nd element removed from list:", listExample)

# to find the index value of the element 5, it gives the first matching values's index
print("location of 5 in the list:", listExample.index(5))

# to find out the number of occurences of a particular value
print("no of times 2 occurs in the list:", listExample.count(2))

# To sort the list, use the sort function
listExample.sort()
print("Sorted List:", listExample)
