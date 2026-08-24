from fastapi import FastAPI

app = FastAPI()

all_customers = [
    {"id":101, "name":"Ravi Kumar","city":"ktm", "risk":"low"},
    {"id":102, "name":"shyam","city":"pkr", "risk":"low"},
    {"id":103, "name":"krishna", "city":"butwal","risk":"low"},
    {"id":104, "name":"janki", "city":"nawalpur","risk":"low"},
    {"id":105, "name":"liladhar","city":"jhapa", "risk":"low"},
]

@app.get("/customers")
def get_customers(city:str, risk:str):
    filtered = [
        c for c in all_customers
        if c["city"] == city and c["risk"] == risk
    ]
    return {
        "city": city,
        "risk": risk,
        "count": len(filtered),
        "results": filtered
    }