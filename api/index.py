import os
from fastapi import FastAPI
#from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from src.core.settings import db_setting
from src.routes.items_route import item_router

# Inisialisasi FastAPI app
app = FastAPI(
    title="Outfit Server",
    description="Backend untuk Outfit",
    version="1.0.0"
)

# CORS middleware


#app.add_middleware(
#    CORSMiddleware,
#    allow_origins=["*"],
#    allow_credentials=True,
#    allow_methods=["*"],
#    allow_headers=["*"],
#)

#setup database
@app.on_event("startup")
def on_startup():
    db_setting()


@app.get("/", response_class=HTMLResponse)
async def root():
    # Baca file HTML langsung
    html_path = os.path.join(os.path.dirname(__file__), "templates", "welcome.html")
    with open(html_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content)

app.include_router(item_router)