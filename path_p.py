from fastapi import FastAPI

app = FastAPI()
customer_risk_profiles = {
    101:{"name":"Ravi Kumar", "risk":"low", "score":0.12},
    102:{"name":"Priya Sharma", "risk":"medium", "score":0.54},
    103:{"name":"Arjun Sharma", "risk":"high", "score":0.89},
}

@app.get("/customer/{customer_id}")
def get_customer_risk(customer_id:int):
    if customer_id not in customer_risk_profiles:
        return {"error":f"customer {customer_id} not found"}


    profile = customer_risk_profiles[customer_id]

    return {
        "customer_id": customer_id,
        "name":profile["name"],
        "risk_level":profile["risk"],
        "score":profile["score"]
    }