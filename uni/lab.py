# key = ["name", "age", "language"]
# value = (['deepak', 21, 'sharma', 'urdu'], ['ali', 23, 'khan', 'urdu'], ['raja', 24, 'khan', 'hindi'])
# for i in range(len(value)):
#     lab = dict(zip(key, value[i]))  
key = ["name", "age", "language"]
value = ['deepak', 21, 'sharma', 'urdu']
lab = dict(zip(key, value))
print(lab)