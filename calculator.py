def add(n1, n2):
    return n1 + n2 

def sub(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": sub,
    "*": multiply,
    "/": divide,
}


adding_numbers = True 

while True: 

    while adding_numbers == True:
        result = 0
        first_number_user = float(input("Whats your first number?"))

        operations_choice = input("which operation do you want to use?\n+\n-\n*\n/\n")

        second_number_user = float(input("Whats your second number"))

        result = operations[operations_choice](first_number_user, second_number_user)

        continue_or_new = input(f"Das Ergebnis ist {result}. Willst du mit dem Ergebnis weiter rechnen y  oder eine neue Rechnung beginnen n: ")
        if continue_or_new == "y":
            adding_numbers = False
            continue
        
         
    while adding_numbers == False:
        operations_choice = input("which operation do you want to use?\n+\n-\n*\n/\n")

        nextnumber = float(input("Whats your number? "))
        result = operations[operations_choice](result,nextnumber)
        continue_or_new = input(f"Das Ergebnis ist {result}. Willst du mit dem Ergebnis weiter rechnen y  oder eine neue Rechnung beginnen n: ")
        if continue_or_new == "n":
            adding_numbers = True
            continue




    