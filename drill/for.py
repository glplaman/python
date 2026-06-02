#  9*9
# homework

for i in range(9):
  for j in range(i+1):
    print(f'{i+1}*{j+1}={(i+1)*(j+1)}\t',end=' ')
    if i==j:
      print()