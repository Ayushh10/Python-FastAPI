from random import randint
from fastapi import FastAPI, HTTPException, Request
from datetime import datetime
from typing import Any
# app = FastAPI(root_path="/api/v1/")
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello world"}

data : Any = [
    {
        "campaign_id": 1,
        "campaign_name": "Summer Launch",
        "date_created": datetime.now(),
        "last_updated": datetime.now()
        },
    {
        "campaign_id": 2,
        "campaign_name": "Winter Launch",
        "date_created": datetime.now(),
        "last_updated": datetime.now()
        }
]

@app.get("/campaigns")
async def campaigns():
    return {"campaings": data}

@app.get("/campaigns/{id}")
async def read_campaigns(id: int):
    for campaign in data:
        if campaign.get("campaign_id") == id:
            return campaign
    raise HTTPException(status_code=404) 

@app.post("/campaigns")
async def create_camp(reqeust: Request):
    body = await reqeust.json()

    new : Any = {
        "campaign_id": randint(10,100),
        "campaign_name": body.get("name"),
        "date_created": body.get("date_created"),
        "last_updated": datetime.now()
    }
    data.append(new)
    return {"data added": new}

