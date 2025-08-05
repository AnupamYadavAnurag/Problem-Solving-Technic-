# Input from the user 
num1 = int(input("Enter the first number: ")) 
num2 = int(input("Enter the second number: ")) 
# Find the smaller number to limit the loop 
if num1 > num2: 
smaller = num2 
else: 
smaller = num1 
# Find HCF using a loop 
for i in range(1, smaller + 1): 
if num1 % i == 0 and num2 % i == 0: 
hcf = i 
# Output the result