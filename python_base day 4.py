# what is return?
def p_plus(a,b):
  print(a+b)

def r_plus(a,b):
  return(a+b)

p_result=p_plus(2,3)
r_result=r_plus(2,3)

print(p_result,r_result)

# example
def plus(a,b):
  return(a+b)
  print("lalala")

result=plus(2,4)
print(result)
# keyword argument
def say_hello(name,age):
  return f"hello {name}, you are {age} right?"

hello=say_hello("Ha_yeon","22")
print(hello)  

# my question
def say_hello():
  print("hello")

hello=say_hello()
print(hello)  
