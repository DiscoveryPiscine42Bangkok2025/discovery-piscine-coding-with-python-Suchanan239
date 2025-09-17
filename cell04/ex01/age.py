age = int(input("Please tell me your age: "))
years = 10
print("You are currently %d years old." %age)
for i in range (0, 3):
  result = age+years
  print("In %d years, you'll be %d years old." %(years,result))
  years += 10