from fastapi import FastAPI

from backend.api import query_routes
from backend.api import upload_routes
from backend.api import health_routes


app = FastAPI(
    title="Multi Agent Research Lab",
    version="1.0"
)


# Register API routes
app.include_router(query_routes.router)
app.include_router(upload_routes.router)
app.include_router(health_routes.router)


@app.get("/")
def root():
    return {"message": "AI Research Lab Backend Running"}




