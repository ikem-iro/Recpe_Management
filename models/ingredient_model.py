from pydantic import BaseModel, Field




class Ingredient(BaseModel):
    ingredient: list[str] = Field(title="Ingredients", description="List of ingredients", example=["flour", "salt"], min_items=1)




