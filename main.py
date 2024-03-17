#from routing import koko
#import routing as koko

import routing

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def aba():
	return {"test":"yep it's already done"}
	
	
	
	
#aba()

#koko.koko()
#routing.koko()
