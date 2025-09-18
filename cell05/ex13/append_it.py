import sys

all_arguments = sys.argv[1:]
keyword = "ism"
if len(all_arguments) != 0:
  for i in all_arguments:
    if keyword in i:
      pass
    else:
      i += keyword
      print(i)
else:
  print("none")