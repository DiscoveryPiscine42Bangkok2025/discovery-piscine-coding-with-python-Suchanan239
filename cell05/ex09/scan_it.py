import sys

all_arg = sys.argv[1:]

if len(all_arg) == 2:
  f_para = all_arg[0]
  s_para = all_arg[1]
  print(s_para.count(f_para))
else:
  print("none")