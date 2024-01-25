#ex1
thisset = {"apple", "banana", "cherry"}
print(thisset)

# Note: the set list is unordered, meaning: the items will appear in a random order.

#ex2
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

#ex3
thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

#ex4
thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)

#ex5
thisset = {"apple", "banana", "cherry"}

print(len(thisset))

#ex6
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

print(set1)
print(set2)
print(set3)

#ex7
set1 = {"abc", 34, True, 40, "male"}

print(set1)

#ex8
myset = {"apple", "banana", "cherry"}

print(type(myset))

#ex9
thisset = set(("apple", "banana", "cherry"))
print(thisset)
# Note: the set list is unordered, so the result will display the items in a random order.

#ex10
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#ex11
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

#ex12
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

#ex13
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

#ex14
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

#ex15
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

#ex16
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

#ex17
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x) #removed item

print(thisset) #the set after removal

#ex18
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

#ex19
thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset) #this will raise an error because the set no longer exists

#ex20
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#ex21
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

#ex22
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

#ex23
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)

#ex24
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)

#ex25
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)

#ex26
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)

#ex27
x = {"apple", "banana", "cherry", True}
y = {"google", 1, "apple", 2}

z = x.symmetric_difference(y)

print(z)
