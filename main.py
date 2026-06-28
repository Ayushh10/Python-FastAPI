from fastapi import FastAPI
from datetime import datetime

app = FastAPI(root_path="/api/v1/")

@app.get("/")
async def root():
    return {"message": "Hello world"}

# def class Campaigns(self):
#     campaign_id = int
#     campaign_name = str
#     date_created = datetime.now()
#     last_updated = datetime.now()

    

Data = Any: [
    {
        campaign_id = int
        campaign_name = str
        date_created = datetime.now()
        last_updated = datetime.now()},
    {}
]
@app.get("/campaigns")
async def campaigns():
    return {"campaings": "Campaign-name"}

@app.post("/campaigns")
async def add_new("campaigns": input()):
    return 
