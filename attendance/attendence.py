roll='''100
 101
 102
 104
 103
 107
110
 123
 128
 136
 139
 141
 142
 147
 149
 164
 169
 177'''
roll=roll.split("\n")
roll=list(map(int,roll))
for i in range(91,181): 
  if i in roll:
    print("p")
  else:
    print("A")
