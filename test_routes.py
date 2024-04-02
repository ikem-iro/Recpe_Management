from fastapi.testclient import TestClient
from main import app
from controllers.recipe_controller import get_recipes, get_one_recipe


client = TestClient(app)


def test_get_all_recipes():
    response = client.get("/v1/api/recipe/get_all_recipes")
    assert response.status_code == 200
    assert response.json() == {"response": get_recipes()}


def test_get_a_recipe():
    response = client.get("/v1/api/recipe/get_recipe/Pancakes")

    assert response.status_code == 200
    assert response.json() == {
        "response": {
            "name": "Pancakes",
            "ingredients": {"flour": "2 cups", "salt": "1 tsp"},
            "instructions": [
                "In a large mixing bowl, combine the dry ingredients. Add the wet ingredients and mix until combined."
            ],
            "category": ["low calorie", "vegan", "low fat"],
        }
    }

    response = client.get("/v1/api/recipe/get_recipe/Doughnut")
    assert response.status_code == 404
    assert response.json() == {"response": {"Error": "Recipe not found"}}


def test_create_a_recipe():
    response = client.post(
        "/v1/api/recipe/create_recipe",
        json={
            "recipe_name": "Waffles",
            "instructions": [
                "In a large mixing bowl, combine the dry ingredients. Add the wet ingredients and mix until combined."
            ],
            "ingredients": {"ingredient": {"flour": "2 cups", "salt": "1 tsp"}},
            "nutritional_info": ["low calorie"],
        },
    )

    assert response.status_code == 201

    assert response.json() == {"response": {"message": "Successfully written to file"}}


def test_edit_a_recipe():
    response = client.patch(
        "/v1/api/recipe/edit_recipe/Waffles",
        json={
            "recipe_name": "Waffles",
            "instructions": [
                "In a large mixing bowl, combine the dry ingredients. Add the wet ingredients and mix until combined."
            ],
            "ingredients": {
                "ingredient": {"flour": "2 cups", "salt": "1 tsp", "sugar": "2 tbsp"}
            },
            "nutritional_info": ["vegan", "low fat"]
        }
    )
    assert response.status_code == 200
    assert response.json() == {"response": "The recipe has been edited."}

    response = client.patch(
        "/v1/api/recipe/edit_recipe/Bread",
        json={
            "recipe_name": "pancakes",
            "instructions": [
                "In a large mixing bowl, combine the dry ingredients. Add the wet ingredients and mix until combined."
            ],
            "ingredients": {
                "ingredient": {
                "flour": "2 cups",
                "salt": "1 tsp",
                "sugar": "2 tbsp"
                }
            },
            "nutritional_info": [
                "low fat"
            ]
        }
    )

    assert response.status_code == 404
    assert response.json() == {"response": {"Error": "Recipe not found"}}


def test_delete_a_recipe():
    response = client.delete("/v1/api/recipe/delete_recipe/Waffles")
    assert response.status_code == 200
    assert response.json() == {"response": "Successfully deleted"}

    response = client.delete("/v1/api/recipe/delete_recipe/Bread")
    assert response.status_code == 404
    assert response.json() == {"response": {"Error": "Recipe not found"}}
