from fastapi import APIRouter, Response
from models.recipe_model import Recipe
from controllers.recipe_controller import (
    create_new_recipe,
    get_recipes,
    get_one_recipe,
    edit_recipe,
    delete_recipe,
)


router = APIRouter(prefix="/api/recipe", tags=["Recipe"])


@router.get("/")
async def root():
    """
    An asynchronous function that handles the root endpoint. It does not take any parameters and returns a dictionary with the message "Hello World".
    """
    return {"message": "Hello World"}


@router.get("/get_all_recipes")
async def get_all_recipe(response: Response):
    """
    A description of the entire function, its parameters, and its return types.
    """
    data = get_recipes()
    response.status_code = 200
    return {"response": data}


@router.get("/get_recipe/{recipe_name}")
async def get_recipe(recipe_name: str, response: Response):
    """
    Retrieve a recipe by the provided recipe name.

    Parameters:
    - recipe_name: a string representing the name of the recipe to retrieve
    - response: a Response object

    Returns:
    - a dictionary containing the response data
    """
    data = get_one_recipe(recipe_name)
    if data == {"Error": "Recipe not found"}:
        response.status_code = 404
        return {"response": data}
    response.status_code = 200
    return {"response": data}


@router.post("/create_recipe")
async def create_recipe(recipe: Recipe, response: Response):
    """
    A route to create a new recipe using the provided recipe data and returns a response with status code 201.
    
    Parameters:
    - recipe: The recipe object containing the details of the new recipe.
    - response: The response object to send back with the created recipe data.
    
    Returns:
    A dictionary with the response data of the created recipe.
    """
    data = create_new_recipe(recipe)

    response.status_code = 201
    return {"response": data}


@router.patch("/edit_recipe/{recipe_name}")
async def edit_a_recipe(recipe_name: str, recipe: Recipe, response:Response):
    """
    Edit a recipe by its name and return a response with the updated status.
    
    Parameters:
        recipe_name (str): The name of the recipe to be edited.
        recipe (Recipe): The updated recipe object.
        response (Response): The FastAPI response object.

    Returns:
        dict: A dictionary containing the response message based on the editing result.
    """
    data = edit_recipe(recipe_name, recipe)
    if data == {"Error": "Recipe not found"}:
        response.status_code = 404
        return {"response": data}

    response.status_code = 200
    return {"response": "The recipe has been edited."}


@router.delete("/delete_recipe/{recipe_name}")
async def delete_a_recipe(recipe_name: str, response: Response):
    """
    Delete a recipe by name.

    Parameters:
    - recipe_name: a string representing the name of the recipe to delete
    - response: a Response object for handling the response

    Returns:
    - A dictionary containing the response message
    """
    data = delete_recipe(recipe_name)
    if data == {"Error": "Recipe not found"}:
        response.status_code = 404
        return {"response": data}
    response.status_code = 200
    return {"response": "Successfully deleted"}
