from fastapi.routing import APIRouter

router = APIRouter()

@router.get("")
def test():
    return 'hello world test'