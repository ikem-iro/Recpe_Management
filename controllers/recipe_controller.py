from utils.file_config import read_file, write_to_file
from uuid import uuid4
from datetime import datetime, timezone


def get_recipes():
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
    recipes = read_file()
    for r in recipes:
        if r["name"] == recipe:
            recipes.remove(r)
            message = write_to_file(recipes)
            return {"message":message, "detail": "Successfully deleted recipe"}
    return {"Error": "Recipe not found"}
