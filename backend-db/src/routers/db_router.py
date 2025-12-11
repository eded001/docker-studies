from fastapi import APIRouter, HTTPException
import asyncpg

router = APIRouter(prefix="/db", tags=["db"])

DATABASE_URL = "postgresql://docker:docker_pass@db:5432/schema"


@router.get("/")
async def db_check():
    try:
        conn = await asyncpg.connect(DATABASE_URL)
        result = await conn.fetchval("SELECT 1")
        await conn.close()

        return {
            "status": "up",
            "db": "connected" if result == 1 else "unexpected response",
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database connection failed: {e}")
