import sys

arguments = sys.argv[1:]
if len(arguments) != 0:
  print("parameters:", len(arguments))
  for i in arguments:
    count = 0
    for char in i:
      count += 1
    print("%s: %d" %(i, count))
else:
  print("none")