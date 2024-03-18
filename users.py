from fastapi import APIRouter 


router = APIRouter()

@router.get("/user", tags=["user"])
async def user_main():
	return {"main": "main"}



@router.get("/user/{id}", tags=["user"])
async def usid(id: int):
	
	#lets convert to a string 
	data_ = str(id)
	
	return {"me":  data_ + " picked user"}
