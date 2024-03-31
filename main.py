import uvicorn
from fastapi import FastAPI
from routes import home_route
from routes import recipe_route


app = FastAPI()
PORT = 5003
host = "127.0.0.1"


app.include_router(home_route.router, prefix='/v1')
app.include_router(recipe_route.router, prefix='/v1')







if __name__ == "__main__":
    uvicorn.run("main:app", host=host, port=PORT, reload=True)