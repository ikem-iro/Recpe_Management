

recipes = []

def get_recipes():
    return recipes

def create_new_recipe(recipe):
    recipe_to_be_added = {
        "name": recipe.recipe_name,
        "ingredients": recipe.ingredients.ingredient,
        "instructions": recipe.instructions,
        "category": recipe.nutritional_info,
    }

    recipes.append(recipe_to_be_added)
    return recipes

def edit_recipe(recipe):
    recipe_to_be_edited = recipe.recipe_name
    
    for r in recipes:
        if recipe_to_be_edited == r["name"]:
           if r["name"] != recipe.recipe_name:
                r["name"] = recipe.recipe_name
           if r["ingredients"] != recipe.ingredients.ingredient:
                r["ingredients"] = recipe.ingredients.ingredient
           if r["instructions"] != recipe.instructions:
                r["instructions"] = recipe.instructions
           if r["category"] != recipe.nutritional_info:
                r["category"] = recipe.nutritional_info

        else:
            return {"Error": "Recipe not found"}
    
    return {"success": "Successfully updated"}


def delete_recipe(recipe):
    recipe_to_delete = recipe
    for r in recipes:
        if r["name"] == recipe_to_delete:
            recipes.remove(r)
            return {"success": "Successfully deleted"}
        else:
            return {"Error": "Recipe not found"}