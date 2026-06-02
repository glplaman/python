for item in [0,1,2,3]:
  print(item)
# or
for item in range(4):
  print(item)

# item still available
print(item)

# string
for item in 'hi,there.':
  print(item)

# break: terminate the for
for item in [0,1,2,3]:
  num=item%2
  print(num)
  if num:
    print(f'in {item}')
    break
  print(f'out {item}')