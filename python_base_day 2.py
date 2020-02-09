#what is set
days={"mon","tue","wed"}
print(type(days))

#what is tuple
days=("mon","tue","wed")
print(type(days))


#what is dictionary
Ha_yeon={
"nickname":"hama",
"age":22,
"Korean": True,
"fav_food":["coffe","waffle"]
}

print(Ha_yeon)

#application 1
Ha_yeon={
"nickname":"hama",
"age":22,
"Korean": True,
"fav_food":["coffe","waffle"]
}

print(Ha_yeon["nickname"])

#application 2
Ha_yeon={
"nickname":"hama",
"age":22,
"Korean": True,
"fav_food":["coffe","waffle"]
}

Ha_yeon["sleepy"]=True

print(Ha_yeon)
