# ###strings 
# name = input("enter your name :")
# # print(len(name))
# print(name.rfind('e'))

##1 program
# validate  user input excersice
#1 .user name no more than 12 characters
#2 .user_name must not  contain space 
#3 .user_name must not contain digits

# user_name = input("enter your user name :")
# if len(user_name) > 12:
#     print("user name must not exceed 12 characters")
# elif not  user_name.find(' ')==-1:
#     print("user name must not contain space")
# elif not  user_name.isalpha():
#     print("user name must not contain digits")
# else:
#     print("welcome",user_name)


###2 program 
# indexing = accessing elements of a sequence using [](indexing operator)
# [start: end :step]
# num = "0123456789"
# print(num[0:5]) #01234
# print(num[0:9:2]) #02468

###3 program
credit_card = "1234-5678-9012-3456"
last_digit = credit_card[::-1]
print(last_digit)