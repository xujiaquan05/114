CREATE TABLE IF NOT EXISTS articles (
    id SERIAL PRIMARY KEY,
    unique_id VARCHAR(64) UNIQUE NOT NULL,
    source_platform VARCHAR(50) NOT NULL,
    board VARCHAR(100),
    title TEXT NOT NULL,
    author VARCHAR(100),
    content TEXT,
    url TEXT,
    push_count INTEGER DEFAULT 0,
    published_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS analysis_results (
    id SERIAL PRIMARY KEY,
    keyword VARCHAR(255) NOT NULL,
    analysis_type VARCHAR(50) NOT NULL,
    result_json JSONB NOT NULL,
    expired_at TIMESTAMP NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS crawl_logs (
    id SERIAL PRIMARY KEY,
    source_platform VARCHAR(50),
    board VARCHAR(100),
    status VARCHAR(50),
    new_count INTEGER DEFAULT 0,
    skipped_count INTEGER DEFAULT 0,
    error_message TEXT,
    started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    finished_at TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_articles_title 
ON articles USING GIN (to_tsvector('simple', title));

CREATE INDEX IF NOT EXISTS idx_articles_content 
ON articles USING GIN (to_tsvector('simple', content));

CREATE INDEX IF NOT EXISTS idx_articles_published_at 
ON articles (published_at);

CREATE INDEX IF NOT EXISTS idx_articles_board 
ON articles (board);