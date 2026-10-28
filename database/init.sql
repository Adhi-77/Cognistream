CREATE TABLE IF NOT EXISTS cognistream.developer_events
(
    event_id String,
    source LowCardinality(String),
    event_type String,
    developer_id String,
    event_timestamp DateTime64(6, 'UTC'),
    repository Nullable(String),
    channel Nullable(String),
    project Nullable(String),
    issue_key Nullable(String),
    ingested_at DateTime64(3, 'UTC') DEFAULT now64(3)
)
ENGINE = MergeTree
ORDER BY (developer_id, event_timestamp, event_id);