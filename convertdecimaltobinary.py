# Python program to convert decimal number into binary number using recursive function
 
def binary(n):
   
   if n > 1:
       binary(n//2)
   print(n % 2,end = '')
 
dec = int(input("Enter an integer: "))
binary(dec)