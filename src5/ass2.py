friends = ("Osama", "Ahmed", "Sayed")
lst = list(friends)
lst[0] = "Elzero"
friends = tuple(lst)
print(friends)
print(type(friends))
print(len(friends), "Elements")

# Needed Output
# ("Elzero", "Ahmed", "Sayed")
# <class 'tuple'>
# 3 Elements
