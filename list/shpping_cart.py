#shoping cart program
foods=[]
price=[]
total=0
while True:
    food =input("enter your favorit food or (q to quit:) ")
    if food.lower()== "q":
        break 
    else:
        foods.append(food)
        prices=float(input("enter prize : "))
        price.append(prices)
print("____your food is here ____")
for food in foods:       
     print(food, end="   ") 
print()
for prices in price:
    print(prices,end="   ")
print()
for prices in price:
    total +=prices
print(f"your total bill is {total}")