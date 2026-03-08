from fastapi import FastAPI

from app.solution_stateless.routes import router as stateless_router
from app.solution_stateful.routes import router as stateful_router

app = FastAPI(
    title="Missing Number API",
    version="1.0",
    description="#### API that extracts a number from 1 to 100 and calculates the missing number.",
    contact={
        "name": "Ariel Plasencia Díaz",
        "email": "arielplasencia00@gmail.com",
    },
    license_info={
        "name": "Next Technologies License",
        "url": "https://www.next-technologies.com.mx/",
    },
)

app.include_router(stateless_router, prefix="/api")
app.include_router(stateful_router, prefix="/api")
