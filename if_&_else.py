# if else
def plus(a,b):
  if type(b)is str:
   return None
  else:
     return a+b


print(plus(12,"19"))

# example
def age_check(age):
  if age < 19 : 
    print(f"you are {age}")
  elif age== 18 or age ==19: 
    print("you are new to this!")

  elif age>20 and age<25:
    print("you are still kind of young")

  else : 
    print("enjoy your drink")


age_check(18)     
