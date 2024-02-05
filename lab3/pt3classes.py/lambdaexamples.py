#example1
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11)) 
print(mytripler(11))

#example2
x = lambda a, b, c: a + b + c
print(x(5, 6, 2))

#example3
def my_func(n):
  return lambda a: a*n

mydoubler =  my_func(2)
print(mydoubler(11))

#example4
def my_func(n):
  return lambda a: a*n

mydoubler = my_func(2)
mytripler = my_func(3)

print(mydoubler(11))
print(mytripler(11))