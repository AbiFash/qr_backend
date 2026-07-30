from fastapi import FastAPI
from routes.qr import router as qr_router
from routes.auth import router as auth_router
from routes.scan import router as scan_router
from routes.assets import router as assets_router


app = FastAPI()

# Register routes
app.include_router(qr_router)
app.include_router(auth_router)
app.include_router(scan_router)
app.include_router(assets_router)

@app.get("/")
def root():
    return {"status": "running"}

