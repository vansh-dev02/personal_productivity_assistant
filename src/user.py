import json
import os


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


DATA_FILE = os.path.join(
    BASE_DIR,
    "data",
    "users.json"
)



class User:

    def __init__(self, name, password):

        self.name = name
        self.password = password



    def save_user(self):

        os.makedirs(
            os.path.dirname(DATA_FILE),
            exist_ok=True
        )


        if not os.path.exists(DATA_FILE):

            with open(DATA_FILE,"w") as file:
                json.dump([],file)



        with open(DATA_FILE,"r") as file:

            users = json.load(file)



        users.append(
            {
                "name": self.name,
                "password": self.password
            }
        )


        with open(DATA_FILE,"w") as file:

            json.dump(
                users,
                file,
                indent=4
            )


        print("User created successfully")




    @staticmethod
    def login(name,password):


        if not os.path.exists(DATA_FILE):

            return False



        with open(DATA_FILE,"r") as file:

            users=json.load(file)



        for user in users:

            if (
                user["name"] == name 
                and 
                user["password"] == password
            ):

                return True



        return False