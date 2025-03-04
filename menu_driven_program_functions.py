def display_menu():
    print("Menu:")
    print("1.Greet User")
    print("2.Check Even/Odd")
    print("3.Exit")
    choice = int(input("Enter your choice (1-3): "))
    return choice


def handle_menu_choice(choice):
    if choice == 1:
        return greet_user()
    if choice == 2:
        return even_odd_checker_action()
    if choice == 3:
        return "Exiting the program....."

    return "Invalid choice! Pls. Enter Between 1 to 3"

def even_odd_checker_action():
    num = int(input("Enter a integer: "))

    if num % 2 == 0:
        return f"{num} is Even number"

    return f"{num} is Odd number"

def greet_user():
    return "Hello! Welcome!"

if __name__ == "__main__":
    while True:
        Output_Menu = display_menu()
        Output_Handle_Menu = handle_menu_choice(Output_Menu)
        print(Output_Handle_Menu + "\n")

        if Output_Menu == 3:
            break
