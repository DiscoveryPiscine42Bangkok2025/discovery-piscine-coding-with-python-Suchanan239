import sys
argument = []
try:
  argument = sys.argv[1]
  print(argument.lower())
except:
  print("none")