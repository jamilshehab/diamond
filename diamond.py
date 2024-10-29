
num=int(input("enter the number of rows : "))
for i in range(0,num):
   for j in range(0,num-i):
       print(" ",end="  ")

   for j in range(1,2*i):
       print("*" , end="  ")
   print()

for i in range(num,0,-1):
   for j in range(num-i):
       print(" ",end="  ")

   for j in range(2*i-1):
       print("*" , end="  ")
   print()

