import time
print('who is the presendent of pakistan')
lis={
  "a":'imran',
  'b':'nawaz',
   'c':'zardari',
   'd':'shahbaz'
}
print('option are')
for i in lis.items():
    time.sleep(1)
    print(i)

user=input('enter a your answer')
if user == 'd':
    time.sleep(1)
    print('your answer is correct')
else:
    time.sleep(1)
    print('your answer is incorrect')
