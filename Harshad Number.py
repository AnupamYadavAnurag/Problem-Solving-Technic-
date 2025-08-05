# Input number from the user 
num = int(input("Enter a number: "))
# Calculate the sum of digits 
sum_of_digits = sum(int(digit) for digit in str(num)) 
# Check if the number is divisible by the sum of its digits 
if num % sum_of_digits == 0:
    print(f"{num} is a Harshad number.")
else:
    print(f"{num} is not a Harshad number.")