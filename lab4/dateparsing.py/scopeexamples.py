#example1
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()

#example2
x = 300

def myfunc():
  x = 200
  print(x)

myfunc()

print(x)
