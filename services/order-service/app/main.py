from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from database import engine, Base
from routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Order Service",
    description="ShopAPI Order Management Service",
    version="1.0.0"
)

Instrumentator().instrument(app).expose(app)

app.include_router(router)

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "order-service"}
