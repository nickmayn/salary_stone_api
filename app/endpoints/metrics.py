from fastapi.routing import APIRouter

router = APIRouter()

@router.get('')
async def general():
    return({
        'average_salary': 1000,
        'std_salary': 400
    })