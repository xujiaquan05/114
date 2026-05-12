from fastapi import FastAPI

from app.core.database import get_db
from app.routers.crawler_router import router as crawler_router

from app.routers import dashboard

app = FastAPI(
    title="Medical Beauty Public Opinion Analysis System",
    description="醫美時尚輿情分析系統 API",
    version="1.0.0"
)


# Đăng ký crawler router vào FastAPI.
# Sau khi include, API /api/crawler/ptt sẽ xuất hiện trong /docs.
app.include_router(crawler_router)

app.include_router(dashboard.router)

@app.get("/")
def root():
    return {
        "message": "Medical Beauty Public Opinion Analysis System API is running"
    }


@app.get("/health")
def health_check():
    """
    Health check dùng để kiểm tra:
    1. Backend có chạy không.
    2. Database có kết nối được không.
    """
    db_status = get_db()

    return {
        "api": "ok",
        "database": db_status
    }