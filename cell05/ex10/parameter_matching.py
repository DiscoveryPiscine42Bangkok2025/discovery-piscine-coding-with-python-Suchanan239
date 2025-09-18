import sys

argument = sys.argv[1]
u_input = input("What was the parameter? ")
if u_input == argument:
  print("Good job!")
else:
  print("Nope, sorry...")