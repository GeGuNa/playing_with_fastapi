from fastapi import APIRouter 


router = APIRouter()

@router.get("/test", tags=["test"])
async def koko():
	return {"kekz": "main"}



@router.get("/test/me", tags=["test"])
async def koko2():
	return {
		"kekz2": """/test/me/  """
	}
