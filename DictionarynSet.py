employeePosition = {
    "Alan": "Sr Developer",
    "John": "Quality Analyst",
    "Jack": "Delivery Manager"
}

# we can access the elements using the following syntax

print("Alan is a", employeePosition["Alan"])

# we can add new values by

employeePosition["Julie"] = "Sales Professional"

print("Julie is a", employeePosition["Julie"])

# we can remove an employee from the dictionary using the del keyword

del employeePosition["John"]

# to demonstrate that John has been removed, we'll loop over the dictionary and print all it's keys and values.

for name, position in employeePosition.items():
    print(name, "is a", position);


''' Sets '''

oscars = {"Jennifer", "Matthew", "Ellen", "Jack", "Leonardo", "Jack"}

print("Stars at the oscars:",oscars);

afterparty = frozenset(["Jennifer", "Neil", "Woody", "Leonardo", "Rachel"])

# to check if Jennifer went to the oscars

print("was Jennifer in the oscars?", "Jennifer" in oscars)

# to perform difference operation, to find who went to oscars but not the after party

print("Stars who came only to the oscars:", oscars - afterparty)

# to perform intersection operation i.e to find out who went to both oscars and the after party

print("Stars who attended both oscars and the after-party:", oscars & afterparty)

# to perform union operation, bring out all distinct values from both sets

print("All stars who were seen:", oscars | afterparty)
