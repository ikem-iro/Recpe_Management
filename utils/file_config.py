import os
import json



RECIPES = []
file_directory = "data"
file = "recipes.json"
file_path = os.path.join(file_directory, file)


def create_file():
    global RECIPES
    global file_directory

    if not os.path.exists(file_directory):
        os.mkdir(file_directory)

    if not os.path.exists(file_path):
        open(file_path, "x")

    if os.path.getsize(file_path) == 0:
        with open(file_path, "w") as f:
            f.write(json.dumps(RECIPES))
            print("Successfully created file")

    with open(file_path, "r") as f:
        data = f.read()
        RECIPES = json.loads(data)
        print("File read successfully")




def read_file():

    with open(file_path, "r") as f:
        data = f.read()
        RECIPES = json.loads(data)
        print("File read successfully")

    return RECIPES


def write_to_file(data):
    RECIPES = data

    with open(file_path, "w") as f:
        f.write(json.dumps(RECIPES, indent=4))
        print("File written successfully")
        return {"message": "Successfully written to file"}
    
