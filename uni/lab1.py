employe=[{"name":"ali","age":23},{'name':'deepak','age':24}]
job=['softwar', 'hardware' ]
import random
for person in employe:
    person[''] =random.choice(job)
    print(person)