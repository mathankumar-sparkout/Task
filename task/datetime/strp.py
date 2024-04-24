from datetime import datetime

str = '2022-01-01 13:30:45'
str1 = datetime.strptime(str, '%Y-%m-%d %H:%M:%S')
print(str1)


str='2024-04-23'
str1=datetime.strptime(str, '%Y-%m-%d')
print(str1)


str='7:30 Am'
str1=datetime.strptime(str,'%H:%M %p')
print(str1)