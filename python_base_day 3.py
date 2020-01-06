# type
age="18"
n_age=int(18)

print(type(age))
print(type(n_age))

# function
def say_hello():
  print("hello")

say_hello()

# input on function(str)
def say_hello(who):
  print("hello",who)

say_hello("Ha_yeon")

# input on function(int)
def plus(a,b):
  print(a+b)

plus(2,3)

# various input
def say_hello(name="A"):
  print("hello",name)

say_hello()
say_hello("B")  
