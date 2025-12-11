from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers.db_router import router as db_router

app = FastAPI(title="API Base", version="1.0.0")

# CORS básico e pragmático
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(db_router)


@app.get("/")
def root():
    return {"message": "Vá para /db para testar a conexão com o banco de dados"}
