age='F'
# break is unnecessary
# _ stands for the default branch
match age:
  case 'm':
    print('male')
  case 'f':
    print('female')
  case _:
    print('the third gender')

# multiple value with |
match age:
  case 'm'|'M'|'male'|'MALE':
    print('male')
  case 'f'|'F'|'female'|'FEMALE':
    print('female')
  case _:
    print('the third gender')