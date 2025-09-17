old_arr = [2, 8, 9, 48, 8, 22,-12, 2]
hold = []
for i in old_arr:
  if i > 5:
    hold.append(i+2)
n_set = set(hold)
new_arr = list(n_set)
print(old_arr)
print(new_arr)