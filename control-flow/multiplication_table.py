number = input("Enter a number to see its multiplication table: ")

# Generate and print the multiplication table from 1 to 10
for i in range(1, 11):
    result = int(number) * i
    print(f"{number} * {i} = {result}")
