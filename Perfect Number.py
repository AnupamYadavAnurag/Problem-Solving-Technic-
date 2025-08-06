 # Input number from the user 
num = int(input("Enter a number: ")) 
# Initialize a variable to store the sum of divisors 
sum_of_divisors = 0 
# Find divisors of the number and add them to sum_of_divisors 
for i in range(1, num):
    if num % i == 0:  # Check if i is a divisor of num 
        sum_of_divisors += i 
# Check if the sum of divisors is equal to the number  
if sum_of_divisors == num: 
    print(f"{num} is a Perfect number.") 
else:
    print(f"{num} is not a Perfect number.")