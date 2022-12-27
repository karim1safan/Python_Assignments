num_one = int(input("X: "))
operation = input("Choose operator: ").strip()
num_two = int(input("Y: "))

match(operation):
    case "+":
        result = num_one + num_two
        print(f"{num_one} + {num_two} = {result}")
    case "-":
        result = num_one - num_two
        print(f"{num_one} - {num_two} = {result}")
    case "*":
        result = num_one * num_two
        print(f"{num_one} * {num_two} = {result}")
    case "/":
        result = num_one / num_two
        print(f"{num_one} / {num_two} = {result}")
