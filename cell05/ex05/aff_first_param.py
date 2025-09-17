import sys
argument = []
try:
  argument = sys.argv[1]
  print(argument)
except:
  print("none")