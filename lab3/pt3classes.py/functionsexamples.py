#example 1
def my_function():
  print("Hello from a function")

my_function()

#example 2
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

#example3
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

#example4
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

#example5
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#example6
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

#example7
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#example8
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

#example9
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

#example10
def myfunction():
  pass

# having an empty function definition like this, would raise an error without the pass statement

#example11
def my_function(x, /):
  print(x)

my_function(3)

#example12
def my_function(x):
  print(x)

my_function(x = 3)

#example13
def my_function(*, x):
  print(x)

my_function(x = 3)

#example14
def my_function(x):
  print(x)

my_function(3)

#example15
def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)

#example16
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
