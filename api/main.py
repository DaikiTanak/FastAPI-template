from fastapi import FastAPI

import api.routers.item as item_router


app = FastAPI()
app.include_router(item_router.router)

@app.get("/health_check")
def health_check():
    return {"message": "ok"}
