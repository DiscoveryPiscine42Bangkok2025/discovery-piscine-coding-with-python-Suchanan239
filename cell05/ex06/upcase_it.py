import sys
argument = []
try:
  argument = sys.argv[1]
  print(argument.upper())
except:
  print("none")