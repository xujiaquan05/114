# backend/app/database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os


# Note:
# Load biến môi trường trong file .env
load_dotenv()


# Note:
# Lấy DATABASE_URL từ file .env
DATABASE_URL = os.getenv("DATABASE_URL")


# Note:
# Nếu DATABASE_URL không tồn tại thì báo lỗi rõ ràng
# để mình biết là file .env chưa đúng.
if DATABASE_URL is None:
    raise ValueError("DATABASE_URL is not set in .env file")


# Note:
# engine là kết nối chính đến PostgreSQL
engine = create_engine(DATABASE_URL)


# Note:
# SessionLocal dùng để tạo session mỗi lần API gọi database
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


# Note:
# Base dùng cho models.py kế thừa
Base = declarative_base()


def get_db():
    """
    Note:
    Đây là function cung cấp database session cho FastAPI.

    FastAPI sẽ gọi hàm này khi thấy:
    db: Session = Depends(get_db)
    """

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()