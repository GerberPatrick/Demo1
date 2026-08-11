from fastapi import APIRouter

router = APIRouter(prefix = "/parameter")

@router.get("/")
def root():
    return "top parameter endpoint"
