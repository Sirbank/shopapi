from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from database import engine, Base
from routes import router

# Create database tables on startup
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Product Service",
    description="ShopAPI Product Management Service",
    version="1.0.0"
)

# Register Prometheus metrics endpoint at /metrics
Instrumentator().instrument(app).expose(app)

# Include routes
app.include_router(router)

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "product-service"}
