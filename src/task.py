import json
import os
from datetime import datetime


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


TASK_FILE = os.path.join(
    BASE_DIR,
    "data",
    "tasks.json"
)



class Task:


    def __init__(self, username, title, priority):

        self.username = username
        self.title = title
        self.priority = priority
        self.status = "Pending"
        self.date = str(datetime.now().date())



    def save_task(self):

        os.makedirs(
            os.path.dirname(TASK_FILE),
            exist_ok=True
        )


        if not os.path.exists(TASK_FILE):

            with open(TASK_FILE,"w") as file:
                json.dump([],file)



        with open(TASK_FILE,"r") as file:

            tasks = json.load(file)



        tasks.append(
            {
                "username": self.username,
                "title": self.title,
                "priority": self.priority,
                "status": self.status,
                "date": self.date
            }
        )



        with open(TASK_FILE,"w") as file:

            json.dump(
                tasks,
                file,
                indent=4
            )


        print("Task added successfully")





    @staticmethod
    def show_tasks(username):


        if not os.path.exists(TASK_FILE):

            print("No tasks found")
            return



        with open(TASK_FILE,"r") as file:

            tasks = json.load(file)



        print("\nYour Tasks:\n")


        count = 1


        for task in tasks:


            if task["username"] == username:


                print(
                    count,
                    "|",
                    task["title"],
                    "| Priority:",
                    task["priority"],
                    "|",
                    task["status"]
                )

                count += 1





    @staticmethod
    def complete_task(username, number):


        with open(TASK_FILE,"r") as file:

            tasks = json.load(file)



        count = 0


        for task in tasks:


            if task["username"] == username:

                count += 1


                if count == number:

                    task["status"] = "Completed"



                    with open(TASK_FILE,"w") as file:

                        json.dump(
                            tasks,
                            file,
                            indent=4
                        )


                    print("Task completed")

                    return



        print("Task not found")





    @staticmethod
    def delete_task(username, number):


        with open(TASK_FILE,"r") as file:

            tasks = json.load(file)



        count = 0

        new_tasks = []



        for task in tasks:


            if task["username"] == username:

                count += 1


                if count == number:

                    continue



            new_tasks.append(task)




        with open(TASK_FILE,"w") as file:

            json.dump(
                new_tasks,
                file,
                indent=4
            )



        print("Task deleted")