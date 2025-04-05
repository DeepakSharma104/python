#1 program
# age=int(input('enter your age for open site:-'))
# if (age >= 100):
#     print("you are too old to sign in ")
# elif age >=18:
#     print("you are now sign up !:")
# elif age <0:
#     print("you have'not been born yet: ")
    
# else:
#     print("you must be 18+ eligible:")


#2 program
# response = input('would you like food ?(y/n): ')
# if response =="y":
#     print('have some food')
# else :
#     print('no food for you')
    
#3program

# name = input('enter your name :')
# if name =="":
#     print(" you did not write your name")
# else:
#     print(f"hello , how are {name}")
 
#4 program
#python weight converter 
# weight = float(input("enter your weight: "))
# unit= input("kilogram or pound (k/l)")
# if unit =="k":
#     weight *= 2.20
#     unit= "lbs"
# elif unit == "l":
#     weight/=2.205
#     unit = 'kgs.'
# else:
#     print(f"{unit} was not valid ")
    
# print(f"your weight is :{weight} {unit} ")


# 5 program
# unit = input("is this temperature is celsius or fahrenheit (c/f )")
# temp= float(input("enter the temperature : "))
# if unit == " c":
#     tem=((temp*9/5)+32)
#     print("the temperature in fehrenheit is {temp} F")
# elif unit == "f":
#     temp = (temp -32)*5/9
#     print("the temperature in celsius is {temp} c")
# else:
#     print (f'{unit} invalid unit of measuement: ')


### condtional expression = A one line shortcut for the if else statement (ternary operator) print or assign one of two  value based on a condition
#x if condition else y  
# num = 77
# result = "even" if num % 2 == 0 else "odd"
# print(result) # even
#6 program
user_role = input("enter your role : ")#admin
access_level  = "full access" if user_role == "admin" else "denied"
print(f"access level: {access_level}")