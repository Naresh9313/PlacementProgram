# n=int(input("Enter Your Number::-"))
# count=0
# i=1

# while(i<=n):
#     if(n%i==0):
#         count+=1
#     i+=1

# if(count==2):
#     print("Prime")

# else:
#     print("Not prime")


# Initialize an empty list to store values
values = []

# Prompt the user to enter 5 numbers
print("Enter 5 numbers:")

# Loop to get 5 inputs from the user
for i in range(5):
    num = int(input(f"Enter number {i + 1}: "))
    values.append(num)

# Display the entered numbers
print("Display numbers:")
for num in values:
    print(num)
