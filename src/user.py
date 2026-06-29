import json
import os


class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password


    def save_user(self):

        if not os.path.exists("data/users.json"):
            with open("data/users.json", "w") as file:
                json.dump([], file)


        with open("data/users.json", "r") as file:
            users = json.load(file)


        users.append({
            "name": self.name,
            "password": self.password
        })


        with open("data/users.json", "w") as file:
            json.dump(users, file, indent=4)


        print("User created successfully")


    @staticmethod
    def login(name, password):

        if not os.path.exists("data/users.json"):
            return False


        with open("data/users.json", "r") as file:
            users = json.load(file)


        for user in users:
            if user["name"] == name and user["password"] == password:
                return True


        return False