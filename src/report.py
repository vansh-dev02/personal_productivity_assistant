import json
import os


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



class Report:


    @staticmethod
    def productivity_score(username):


        if not os.path.exists(TASK_FILE):

            print("No tasks available")
            return



        with open(TASK_FILE,"r") as file:

            tasks = json.load(file)



        total = 0
        completed = 0



        for task in tasks:


            if task["username"] == username:


                total += 1


                if task["status"] == "Completed":

                    completed += 1




        if total == 0:

            print("No tasks found")
            return



        score = (completed / total) * 100



        print("\n===== Productivity Report =====")


        print("Total Tasks:", total)

        print("Completed:", completed)

        print(
            "Pending:",
            total-completed
        )


        print(
            "Productivity Score:",
            round(score,2),
            "%"
        )


        if score >= 80:

            print("Excellent work 🔥")


        elif score >= 50:

            print("Good progress 👍")


        else:

            print("Need more focus 💪")