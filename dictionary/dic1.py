# dictionary = collection of {key :value }pairs  
#  ordered, mutable, and changeable , no duplicate 

capital ={'USA':'Washington DC', 'India':'Delhi', 'Japan':'Tokyo',"pakistan":"Islamabad"}
print(capital)
print(len(capital)) #length of dictionary
# Accessing items in dictionary
print(capital['India']) #Accessing value using key
# Adding items in dictionary
capital['France'] = 'Paris'
print(capital)
# Removing items in dictionary
capital.pop('Japan')
print(capital)
# Removing last inserted item
capital.popitem()
print(capital)


# Dictionary methods
print(capital.keys()) # This will raise an error because capital is deleted
print(capital.values()) # This will raise an error because capital is deleted
print(capital.items()) # This will raise an error because capital is deleted