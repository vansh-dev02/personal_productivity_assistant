import json
import os
from datetime import datetime


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


NOTE_FILE = os.path.join(
    BASE_DIR,
    "data",
    "notes.json"
)



class Note:


    def __init__(self, username, title, content):

        self.username = username
        self.title = title
        self.content = content
        self.date = str(datetime.now().date())



    def save_note(self):

        os.makedirs(
            os.path.dirname(NOTE_FILE),
            exist_ok=True
        )


        if not os.path.exists(NOTE_FILE):

            with open(NOTE_FILE,"w") as file:
                json.dump([],file)



        with open(NOTE_FILE,"r") as file:

            notes = json.load(file)



        notes.append(
            {
                "username": self.username,
                "title": self.title,
                "content": self.content,
                "date": self.date
            }
        )



        with open(NOTE_FILE,"w") as file:

            json.dump(
                notes,
                file,
                indent=4
            )


        print("Note saved successfully")





    @staticmethod
    def show_notes(username):


        if not os.path.exists(NOTE_FILE):

            print("No notes found")
            return



        with open(NOTE_FILE,"r") as file:

            notes=json.load(file)



        print("\nYour Notes:\n")



        for note in notes:


            if note["username"] == username:


                print(
                    "Title:",
                    note["title"]
                )

                print(
                    "Content:",
                    note["content"]
                )

                print(
                    "Date:",
                    note["date"]
                )

                print("----------------")