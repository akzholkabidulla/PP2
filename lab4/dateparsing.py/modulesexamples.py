#example 1
def greeting(name):
    print("Hello,"+name)
#save this code in a file named "mymodule.py"
    
#example2
import mymodule

mymodule.greeting("Amigo")

#example3
person1={
    "name" : "Matt", 
    "age" : 27,
    "country" : "England"  
}  # save this code in a file named "mymodule2.py"

import mymodule2
a = mymodule2.person["age"]
print(a)

#example4
import mymodule as mx
a= mx.person1["age"]
print(a) #create an alias for mymodule called mx

#example5
def greeting(name):
  print("Hello, " + name)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

from mymodule import person1

print (person1["age"])