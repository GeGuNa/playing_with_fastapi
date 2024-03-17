#from routing import koko
#import routing as koko

import routing

from fastapi import FastAPI

app = FastAPI()


app.include_router(routing.router)



@app.get("/")
def aba():
	return {"test":"yep it's already done"}
	
@app.get("/about")
def aba3():
	return {"xz":"xzzz"}
	
	
@app.get("/contact")
def aba4():
	return {"cnt":"xzzz"}	
	
	
@app.get("/blog")
def aba4():
	return {"cnt":"blog"}	
	
@app.get("/blog/{id}")
def aba44(id: int):
	return {"cnt": id}			
	
	
@app.get("/blog/{id}/edit/{edit}")
def aba44(id: int, edit: str):
	return {"post_id": id, "edit": edit + " edit_string id"}		
	
#aba()

#koko.koko()
#routing.koko()
