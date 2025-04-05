# name= input('enter your name')
# while  name =="":
#     print("You didn't enter your name: ")
#     break
# else:
#     print("Hello " + name)


###2 program
# age = int(input("Enter your age: "))
# while age <0:
#     print("Age cannot be negative. Please enter a valid age.")
#     age = int(input("Enter your age: "))
# else:
#     print("Your age is:", age)
#     while age <18:
#         print("You are not an adult.")
#         age = int(input("Enter your age: "))
     
#     else:
#       print(f"You are an adult, visit this link: https://chatgpt.com/")


# 3 program  ad to cart 
# food = input("Enter your favorite food or (q to quit): ")
# list = []
# while food != "q":
#     print("Your favorite food is:", food)
#     list.append(food)
#     if food == "piza":
#         print("Pizza price is 100")
#     elif food == "burger":
#         print("Burger price is 50")
#     elif food == "samosa":
#         print("Samosa price is 20")
#     else:
#         print("Food not available") 
#     food = input("Enter your favorite food or (q to quit): ")
# print("Your favorite foods are:", list)
# print("Thank you for shopping with us!")

### 4 program


# num= int(input("Enter number:btw 1 to 10 "))
# while num <1 or num>10:
#     print(f"Number is not in range {num}")
#     num= int(input("Enter number:btw 1 to 10"))
   
# print("Number is in range")


### 5 program find speed 
distance = int(input("Enter distance in km: "))
time = int(input("Enter time in hours: "))
speed = distance / time
print("Speed is:", speed, "km/h")
if speed > 60:
    print("You are over speeding")
elif speed < 60:
    print("You are under speeding")
else:
    print("You are driving at a normal speed")
# print("Thank you for using our speed calculator")
