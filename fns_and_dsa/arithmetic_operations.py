def perform_operation(num1, num2, operation):
    match operation:
        case "add":
            return num1 + num2
        case "subtraction":
            return num1 - num2
        case "multiply":
            return num1 * num2
        case "divide":
            try:
                result = num1 / num2
                return result
            except Exception as error:
                print(f"An error occurred: {error}")
