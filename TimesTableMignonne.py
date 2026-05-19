# 1. Ask the user for a positive integer
user_num = int(input("Enter a positive integer: "))

# 2. Set the starting multiplier to 10
multiplier = 10

print(f"\nMultiplication Table for {user_num} (from 10 to 20):")

# 3. Use a while loop to print the table from 10 up to 20
while multiplier <= 20:
    # Calculate the result
    result = user_num * multiplier
    
    # Print the formatted line
    print(f"{user_num} x {multiplier} = {result}")
        
    # 4. Increment the multiplier to avoid an infinite loop
    multiplier += 1
