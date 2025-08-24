import os
from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from src.core.settings import db_setting
from src.routes.catalog_route import router as catalog_router
from src.routes.product_router import router as product_router
from src.routes.item_router import router as item_router


#setup database
@asynccontextmanager
async def lifespan(app: FastAPI):
    db_setting()
    yield
    print("App shutdown...")

# Inisialisasi FastAPI app
app = FastAPI(
    title="Outfit Server",
    description="Backend untuk Outfit",
    version="1.0.0",
    lifespan=lifespan
)

# CORS middleware


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/", response_class=HTMLResponse)
async def root():
    # Baca file HTML langsung
    html_path = os.path.join(os.path.dirname(__file__), "templates", "welcome.html")
    with open(html_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content)

app.include_router(catalog_router)
app.include_router(product_router)
app.include_router(item_router)