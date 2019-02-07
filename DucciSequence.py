
import sys

# Link https://www.reddit.com/r/dailyprogrammer/comments/8sjcl0/20180620_challenge_364_intermediate_the_ducci/
#                               OUTPUT
# Your program should emit the number of steps taken to get to either an all 0 tuple or 
# when it enters a stable repeating pattern.

def list_sum(list):
    sum = 0
    for i in range (len(list)):
        sum = sum + list[i]
    return sum


list = []
list_2 = []
count = 0
v_i = 0
raw_input("Insert 4 integer:\n")
for i in range (0,4):
    n = int(raw_input())
    list.append(n)

while (list_sum(list)!=0):
    for i in range (len(list)):
        if i == 3:
            v_i = abs(list[i] - list[0])
            list_2.append(v_i)
        else:
            v_i = abs(list[i]-list[i+1])
            list_2.append(v_i)
            
    count = count +1
    print(list_2)
    list = list_2
    list_2 = []

print(count)
