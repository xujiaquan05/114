# backend/app/services/cache_service.py

from datetime import datetime, timedelta


# Note:
# Đây là cache tạm lưu trong RAM.
# Key là điều kiện query.
# Value là dữ liệu dashboard + thời gian hết hạn.
CACHE_STORE = {}


def get_cache(key: str):
    """
    Note:
    Lấy dữ liệu cache theo key.

    Nếu:
    - key không tồn tại => return None
    - cache hết hạn => xóa cache rồi return None
    - cache còn hạn => return data
    """

    cache_item = CACHE_STORE.get(key)

    if cache_item is None:
        return None

    expires_at = cache_item["expires_at"]

    if datetime.utcnow() > expires_at:
        del CACHE_STORE[key]
        return None

    return cache_item["data"]


def set_cache(key: str, data, minutes: int = 30):
    """
    Note:
    Lưu dữ liệu vào cache.

    minutes = 30 nghĩa là:
    trong 30 phút nếu user query cùng điều kiện,
    backend sẽ trả cache thay vì query database lại.
    """

    CACHE_STORE[key] = {
        "data": data,
        "expires_at": datetime.utcnow() + timedelta(minutes=minutes),
    }