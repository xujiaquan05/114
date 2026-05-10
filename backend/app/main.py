from fastapi import FastAPI
from app.core.database import test_database_connection

app = FastAPI(
    title="Medical Beauty Public Opinion Analysis System",
    description="醫美時尚輿情分析系統 API",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "Medical Beauty Public Opinion Analysis System API is running"
    }

@app.get("/health")
def health_check():
    db_status = test_database_connection()

    return {
        "api": "ok",
        "database": db_status
    }