import sys

keyword = "z"
all_arguments = sys.argv[1:]
if len(all_arguments) != 0:
  argument = all_arguments[0]
  count = argument.count(keyword)
  if count == 0:
    print("none")
  else:
    for i in range(0, count):
      print(keyword, end="")
else:
  print("none")