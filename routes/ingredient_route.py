from fastapi import APIRouter, Response
from models.ingredient_model import Ingredient

from controllers.ingredient_controller import create_new_ingredient



router = APIRouter(prefix='/api/ingredient', tags=['Ingredient'])
@router.get('/')
async def root():
    """
    Endpoint for the root URL, returns a dictionary with a 'message' key containing 'Hello World'.
    """
    return {"message": "Hello World"}



@router.post('/add_ingredient')
async def add_ingredient(ingredient: Ingredient, response: Response):
    """
    A description of the entire function, its parameters, and its return types.
    """
    data = create_new_ingredient(ingredient)

    response.status_code = 201
    return {"response": data}