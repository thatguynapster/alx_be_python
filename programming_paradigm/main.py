# from practice_exercise_student import Student

# student_name = input('Enter student name:')
# student_age=input('Enter student age:')

# student = Student(student_name, student_age)

# print(student.get_student_details())


from practice_exercise_product_catalog import Product

# product1 = Product("Laptop", 1200, 10)
# product2 = Product("Mobile Phone", 699, 8)
# product3 = Product("Tablet", 899, 15)

# print(f'{product1.name} total value: {product1.get_products_value()}')
# print(f'{product2.name} total value: {product2.get_products_value()}')
# print(f'{product3.name} total value: {product3.get_products_value()}')


# users can add multiple products
def add_product():
    name = input("Enter product name:")

    while True:
        try:
            price = float(input("Enter product price:"))
            break
        except ValueError:
            print("Invalid price. Please enter a number.")

    while True:
        try:
            quantity = int(input("Enter product quantity"))
            break
        except ValueError:
            print("Invalid quantity. Please enter an integer")

    return Product(name, price, quantity)


products = []

while True:
    print("\nAdd new product")
    product = add_product()
    products.append(product)

    more = input("Do you wan tto add another product? (yes/no):").lower()
    if more != "yes":
        break


print("\nProduct Catalog Summary:")
for prod in products:
    print(
        f"{prod.name} - Price: {prod.price}, Quantity: {prod.quantity}, Total Value: {prod.get_products_value()}"
    )
