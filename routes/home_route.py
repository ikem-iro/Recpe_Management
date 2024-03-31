from fastapi import APIRouter

router = APIRouter(prefix='/api', tags=['Home'])


@router.get('/')
async def root():
    return {"message": "Hello World"}