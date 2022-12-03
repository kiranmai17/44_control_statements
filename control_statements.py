'''
DAY:saturday
DATE:3rd  dec 2022
TOPIC:control statements
AUTHOR:kiranmai
'''
a,b=(int(x) for x in input().split())
if(a<b):print(f'{a} is less than {b}')
elif(a>b):print(f"{a} is greater than {b}")
elif(a<=b):print(f"{a} is less than or equalto{b}")
elif(a>=b):print(f"{a} isgreaterthanorequalto{b}")
elif(a!=b):print(f"{a} is not equal to {b}")
elif(a==b):print(f"{a} is equal to {b}")
#a=9 b=9: 9 is less than or equalto9
#(in elif only one condition will execute)
