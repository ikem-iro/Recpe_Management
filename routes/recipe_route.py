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
    return {"message": "Hello World"}


@router.get("/get_all_recipes")
async def get_all_recipe(response: Response):
    data = get_recipes()
    response.status_code = 200
    return {"response": data}


@router.get("/get_recipe/{recipe_name}")
async def get_recipe(recipe_name: str, response: Response):
    data = get_one_recipe(recipe_name)
    if data == {"Error": "Recipe not found"}:
        response.status_code = 404
        return {"response": data}
    response.status_code = 200
    return {"response": data}


@router.post("/create_recipe")
async def create_recipe(recipe: Recipe, response: Response):
    data = create_new_recipe(recipe)

    response.status_code = 201
    return {"response": data}


@router.patch("/edit_recipe/{recipe_name}")
async def edit_a_recipe(recipe_name: str, recipe: Recipe, response:Response):
    data = edit_recipe(recipe_name, recipe)
    if data == {"Error": "Recipe not found"}:
        response.status_code = 404
        return {"response": data}

    response.status_code = 200
    return {"response": "The recipe has been edited."}


@router.delete("/delete_recipe/{recipe_name}")
async def delete_a_recipe(recipe_name: str, response: Response):
    data = delete_recipe(recipe_name)
    if data == {"Error": "Recipe not found"}:
        response.status_code = 404
        return {"response": data}
    response.status_code = 200
    return {"response": "Successfully deleted"}
