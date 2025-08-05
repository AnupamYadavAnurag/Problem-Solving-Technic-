 # Input number from the user 
• num = int(input("Enter a number: ")) 
• # Square the number 
• square = num * num 
• # Convert both the number and its square to strings to compare their 
endings 
• str_num = str(num) 
• str_square = str(square) 
• # Check if the square ends with the number itself 
• if str_square.endswith(str_num): 
•    print(f"{num} is an Automorphic number.") 
• else: 
•    print(f"{num} is not an Automorphic number.")