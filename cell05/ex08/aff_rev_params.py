import sys

arguments = sys.argv[1:]

if len(arguments) < 2:
  print("none")
else:
  for i in reversed(arguments):
    print(i)