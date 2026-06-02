
age=18
URL='glplaman.github.io'
# print
# 拼接字符串，会在 age 变量前后自动添加空格
# 可读性低：当变量变多时，引号和逗号的嵌套会让代码难以阅读
# 大多数现代 Python 环境（尤其是 Linux/Mac）中，直接使用 \n 或多次 print
print('hi, i am ',age,';\r\nmy repository is ',URL)

# with f-string
# start with f
print(f'hi,i am {age};\nmy repository is {URL}')