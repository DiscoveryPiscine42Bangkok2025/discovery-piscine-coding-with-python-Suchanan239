import sys

range_list = []
all_argument = sys.argv[1:]
if len(all_argument) != 0:
  f_num = int(all_argument[0])
  s_num = int(all_argument[1])
  for num in range (f_num, s_num+1):
    range_list.append(num)
  print(range_list)
else:
  print("none")