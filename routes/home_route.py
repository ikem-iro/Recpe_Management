from fastapi import APIRouter

router = APIRouter(prefix='/api', tags=['Home'])


@router.get('/')
async def root():
    """
    A function that handles the root endpoint and returns a JSON message.
    """
    return {"message": "Hello World"}