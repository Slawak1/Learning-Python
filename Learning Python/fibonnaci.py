# Slawomir Sowa
# Date: 23/02/2019
# Write program prints Fibonacci Sequence.

number = 30

f_list = [0,1]

for i in range(0, number):
     
    c = f_list[-1] + f_list[-2]
    f_list.append(c)
    

print (f_list)

