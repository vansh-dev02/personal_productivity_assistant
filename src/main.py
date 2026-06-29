from user import User


print("===== Personal Productivity Assistant =====")


choice = input(
"""
1. Create Account
2. Login

Choose:
"""
)


if choice == "1":

    name = input("Enter name: ")
    password = input("Enter password: ")

    user = User(name,password)
    user.save_user()


elif choice == "2":

    name = input("Name: ")
    password = input("Password: ")

    if User.login(name,password):
        print("Login successful")

    else:
        print("Invalid details")