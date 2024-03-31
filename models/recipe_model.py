from pydantic import BaseModel, Field
from enum import Enum


class NutritionalInfo(str, Enum):
    low_calorie = "low calorie"
    vegan = "vegan"
    low_carb = "low carb"
    low_sodium = "low sodium"
    low_sugar = "low sugar"
    low_fat = "low fat"


class Ingredients(BaseModel):
    ingredient: dict[str, str] = Field(title="Ingredients", description="List of ingredients and their quantities", example={"flour": "2 cups", "salt": "1 tsp"}, min_items=1)


class Recipe(BaseModel):
    recipe_name:str = Field(title="Name", description="Name of the recipe", example="Pancakes", min_length=2, pattern="^[a-zA-Z]+$")
    instructions: list[str] = Field(title="Instructions",description="List of instructions", example=["In a large mixing bowl, combine the dry ingredients. Add the wet ingredients and mix until combined."], min_items=1)
    ingredients:Ingredients
    nutritional_info: list[NutritionalInfo] = Field(default=None, description="List of nutritional info", example=["low calorie", "vegan", "low fat"], min_items=0)