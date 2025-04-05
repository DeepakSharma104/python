num1=int(input("enter a number:\n"))
num2=int(input("enter a  second number:\n"))
operator=input('chose any operator like +,-,%, *,/,//,**:\n')
if operator =='+':
    print(num1+num2)
elif operator =='-':
    print(num1-num2)
elif operator =='*':
    print(num1*num2)
elif operator =='%':
    print(num1%num2)
elif operator =='/':
    if num2 !=0:
     print(num1/num2)
else:
    print('undefine')
 