#Factorial of a number

p = 1 #assign a variable as 1 
n = int(input("Enter a Number: "))
for i in range(1,n+1): #initiate loop from 1 to n+1
    p = p*i

print("The factorial of the given number:" , p)