# import time
# time.sleep(2)
# for i in range(1, 11,1):
#     if i == 5:
#         print("Found 5, breaking the loop.")
#         break
#     print(i)
# print("End of loop")
#2 program
import time 
my_time=int(input('enter you time:'))
for x in range (1,my_time):
    second=x%60
    print(f"00:00:{second:02}")
    time.sleep(1)
print("time up")