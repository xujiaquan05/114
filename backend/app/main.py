from fastapi import FastAPI
from app.core.database import test_database_connection, SessionLocal
from app.services.article_service import create_article

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


@app.post("/test/create-article")
def test_create_article():
    db = SessionLocal()

    try:
        article, is_new = create_article(
            db=db,
            unique_id="test_article_001",
            platform_name="ptt",
            board_name="BeautySalon",
            author_username="test_user",
            title="測試文章：玻尿酸心得",
            content="這是一篇測試文章，用來確認 articles insert 是否正常。",
            url="https://www.ptt.cc/bbs/BeautySalon/test.html",
            push_count=10,
            published_at=None
        )

        return {
            "success": True,
            "is_new": is_new,
            "article_id": article.id,
            "title": article.title
        }

    finally:
        db.close()