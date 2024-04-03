from utils.file_config import read_file, write_to_file
from uuid import uuid4
from datetime import datetime, timezone


def get_recipes():
    """
    Get recipes from a file and format them into a list of dictionaries with specific keys.
    """
    recipes = read_file()
    returned_recipes = []

    for r in recipes:
        new_recipe_obj = {
            "name": r["name"],
            "ingredients": r["ingredients"],
            "instructions": r["instructions"],
            "category": r["category"],
        }
        returned_recipes.append(new_recipe_obj)

    return returned_recipes


def get_one_recipe(recipe_name):
    """
    This function takes a recipe name as input and returns the details of the recipe including its name, ingredients, instructions, and category. If the recipe is not found, it returns an error message.
    """
    recipes = []
    recipes = read_file()
    obj_to_return = {}
    for r in recipes:
        if r["name"] == recipe_name:
            obj_to_return = {
                "name": r["name"],
                "ingredients": r["ingredients"],
                "instructions": r["instructions"],
                "category": r["category"],
            }

            return obj_to_return

    return {"Error": "Recipe not found"}


def create_new_recipe(recipe):
    """
    Creates a new recipe by adding the provided recipe information to the existing list of recipes.
    
    Parameters:
        recipe (object): The recipe object containing recipe_name, ingredients, instructions, nutritional_info.

    Returns:
        str: A message indicating the success or failure of writing the updated recipe list to a file.
    """
    recipes = []
    recipes = read_file()
    recipe_to_be_added = {
        "_id": str(uuid4()),
        "name": recipe.recipe_name,
        "ingredients": recipe.ingredients.ingredient,
        "instructions": recipe.instructions,
        "category": recipe.nutritional_info,
        "timestamps": {
            "created_at": datetime.now(timezone.utc).isoformat(),
            "updated_at": datetime.now(timezone.utc).isoformat(),
        },
    }

    recipes.append(recipe_to_be_added)
    message = write_to_file(recipes)
    return message


def edit_recipe(recipe_name, recipe):
    """
    Edit a recipe in the file by modifying the attributes of the existing recipe object.
    
    Args:
        recipe_name (str): The name of the recipe to be edited.
        recipe (object): The new recipe object containing the updated attributes.

    Returns:
        dict: If the recipe to be modified is not found, returns a dictionary with an error message. 
        If the modification is successful, returns a message indicating the success of the operation.
    """
    recipes = read_file()
    recipe_to_modify = None

    for r in recipes:
        if recipe_name == r["name"]:
            recipe_to_modify = r
            break

    if recipe_to_modify is None:
        return {"Error": "Recipe not found"}

    # Update the attributes of the existing recipe object
    recipe_to_modify["name"] = recipe.recipe_name
    recipe_to_modify["ingredients"] = recipe.ingredients.ingredient
    recipe_to_modify["instructions"] = recipe.instructions
    recipe_to_modify["category"] = recipe.nutritional_info  # Assuming recipe.category corresponds to the category attribute
    recipe_to_modify["timestamps"]["updated_at"] = datetime.now(timezone.utc).isoformat()

    # Write modified recipes back to the file
    message = write_to_file(recipes)
    return message


def delete_recipe(recipe):
    """
    Delete a recipe from the list of recipes.
    
    Parameters:
    recipe (str): The name of the recipe to be deleted.
    
    Returns:
    dict: A dictionary containing a message and details of the deletion operation.
           If successful, returns {"message": str, "detail": str}.
           If the recipe is not found, returns {"Error": "Recipe not found"}.
    """
    recipes = read_file()
    for r in recipes:
        if r["name"] == recipe:
            recipes.remove(r)
            message = write_to_file(recipes)
            return {"message":message, "detail": "Successfully deleted recipe"}
    return {"Error": "Recipe not found"}
