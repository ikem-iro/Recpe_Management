import os
import json



RECIPES = []
file_directory = "data"
file = "recipes.json"
file_path = os.path.join(file_directory, file)


def create_file(): #pragma no cover
    """
    A function to create a file if it doesn't exist and read/write recipe data to it.
    """
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




def read_file(): #pragma no cover
    """
    This function reads a file from the specified file path and loads the content as JSON.
    It returns the loaded JSON data.
    """

    with open(file_path, "r") as f:
        data = f.read()
        RECIPES = json.loads(data)
        print("File read successfully")

    return RECIPES


def write_to_file(data): #pragma no cover
    """
    Write the provided data to a file specified by the file path.

    Parameters:
    - data: the data to be written to the file

    Returns:
    - A dictionary with a message indicating the write status
    """
    RECIPES = data

    with open(file_path, "w") as f:
        f.write(json.dumps(RECIPES, indent=4))
        print("File written successfully")
        return {"message": "Successfully written to file"}
    
