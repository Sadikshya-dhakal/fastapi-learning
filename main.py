from fastapi import FastAPI

app = FastAPI()

@app.get("/") #decorator 
def home():
    return {"message":"my fast api is working"}

@app.get("/about")
def about():
    return {"priject":"Loan risk model"}