u_input = input()

for i in u_input:
  if(i.islower()):
    print(i.upper(), end="")
  elif(i == " "):
    print(" ", end="")
  elif(i.isupper()):
    print(i.lower(), end="")
  else:
    print(i, end="")