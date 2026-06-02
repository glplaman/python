# IF-ELSE
# single branch
age=int(input('your age:'))
if(age>18):
  print('adult')
else:
  print('teenager')

# multiple branch
# grade
# best pratice: without bracket
score=int(input('your score:'))
if score>=90:
  print('A')
elif  score>=80:
  print('B')
elif score>=70:
  print('C')
elif score>=60:
  print('D')
else:
  print('F')


# when to use bracket
#   and or ...
#   long statement


# Ternary Operator
# also known as Conditional Expression
# as a result
tips='adult' if age>=18 else 'teenager'