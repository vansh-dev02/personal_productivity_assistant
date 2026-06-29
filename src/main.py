from user import User
from task import Task
from notes import Note
from report import Report


print("===== Personal Productivity Assistant =====")


while True:

    print("""
1. Create Account
2. Login
3. Exit
""")


    choice = input("Choose: ")



    if choice == "1":

        name = input("Enter username: ")
        password = input("Enter password: ")

        user = User(name, password)

        user.save_user()



    elif choice == "2":

        name = input("Enter username: ")
        password = input("Enter password: ")



        if User.login(name,password):

            print("\nLogin successful")


            while True:


                print("""
1. Add Task
2. View Tasks
3. Complete Task
4. Delete Task
5. Add Note
6. View Notes
7. Productivity Report
8. Logout
""")


                option = input("Choose: ")



                if option == "1":

                    title = input("Task name: ")

                    priority = input(
                        "Priority (High/Medium/Low): "
                    )


                    task = Task(
                        name,
                        title,
                        priority
                    )

                    task.save_task()



                elif option == "2":

                    Task.show_tasks(name)



                elif option == "3":

                    Task.show_tasks(name)

                    number = int(
                        input("Enter task number to complete: ")
                    )


                    Task.complete_task(
                        name,
                        number
                    )



                elif option == "4":

                    Task.show_tasks(name)

                    number = int(
                        input("Enter task number to delete: ")
                    )


                    Task.delete_task(
                        name,
                        number
                    )



                elif option == "5":

                    title = input("Note title: ")

                    content = input("Write note: ")


                    note = Note(
                        name,
                        title,
                        content
                    )


                    note.save_note()



                elif option == "6":

                    Note.show_notes(name)



                elif option == "7":

                    Report.productivity_score(name)



                elif option == "8":

                    print("Logged out")

                    break




        else:

            print("Invalid username or password")




    elif choice == "3":

        print("Goodbye")

        break