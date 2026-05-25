from fastapi import APIRouter

router = APIRouter(
    prefix="/reefvive",
    tags=["Reefvive"]
)

@router.get("/hello")
def hello():
    return "Hello, reefvive!"