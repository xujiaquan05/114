from datetime import datetime

from app.models.database_models import CrawlLog


def create_crawl_log(db, platform_id=None, board_id=None, status="running"):
    """
    Tạo log khi crawler bắt đầu chạy.

    Vì sao cần log?
    Để sau này biết crawler có chạy không, chạy lúc nào,
    thành công hay thất bại, lấy được bao nhiêu bài mới.
    """
    crawl_log = CrawlLog(
        platform_id=platform_id,
        board_id=board_id,
        status=status,
        new_count=0,
        skipped_count=0,
        started_at=datetime.now()
    )

    db.add(crawl_log)
    db.commit()
    db.refresh(crawl_log)

    return crawl_log


def finish_crawl_log(
    db,
    crawl_log,
    status="success",
    new_count=0,
    skipped_count=0,
    error_message=None
):
    """
    Cập nhật log sau khi crawler chạy xong.

    Nếu thành công:
        status = success

    Nếu thất bại:
        status = failed
        error_message = nội dung lỗi
    """
    crawl_log.status = status
    crawl_log.new_count = new_count
    crawl_log.skipped_count = skipped_count
    crawl_log.error_message = error_message
    crawl_log.finished_at = datetime.now()

    db.commit()
    db.refresh(crawl_log)

    return crawl_log