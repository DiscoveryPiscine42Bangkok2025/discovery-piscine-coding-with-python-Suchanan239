import sys
import re

all_arg = sys.argv[1:]

if len(all_arg) == 2:
  f_para = all_arg[0]
  s_para = all_arg[1]
  count = re.findall(f_para, s_para)
  print(len(count))
else:
  print("none")
