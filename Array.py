values = []
print("Enter 5 numbers:")
for i in range(5):
    num = int(input(f"Enter number {i + 1}: "))
    values.append(num)
print("Display numbers:")
for num in values:
    print(num)
