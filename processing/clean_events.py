import json
from pathlib import Path

import polars as pl


def load_events(raw_dir: Path) -> list[dict]:
    """Load JSON events from every source file."""
    events = []

    for file_path in sorted(raw_dir.glob("*_events.json")):
        with file_path.open("r", encoding="utf-8") as file:
            file_events = json.load(file)

        if not isinstance(file_events, list):
            print(f"Skipping invalid JSON structure: {file_path.name}")
            continue

        print(f"Loaded {len(file_events)} events from {file_path.name}")
        events.extend(file_events)

    return events


def clean_events(events: list[dict]) -> pl.DataFrame:
    """Standardize fields and remove invalid or duplicate events."""
    if not events:
        return pl.DataFrame(
            schema={
                "event_id": pl.String,
                "source": pl.String,
                "event_type": pl.String,
                "developer_id": pl.String,
                "timestamp": pl.String,
            }
        )

    df = pl.DataFrame(events, infer_schema_length=None)

    required_columns = [
        "event_id",
        "source",
        "event_type",
        "developer_id",
        "timestamp",
    ]

    # Add required columns if a source event is missing one.
    for column in required_columns:
        if column not in df.columns:
            df = df.with_columns(pl.lit(None).alias(column))

    # Standardize required text fields.
    for column in required_columns:
        df = df.with_columns(
            pl.col(column)
            .cast(pl.String, strict=False)
            .str.strip_chars()
            .replace("", None)
            .alias(column)
        )

    # Remove rows without essential identifying information.
    df = df.drop_nulls(subset=required_columns)

    # Parse timestamps. Invalid timestamps become null and are removed.
    df = df.with_columns(
        pl.col("timestamp")
        .str.to_datetime(time_zone="UTC", strict=False)
        .alias("timestamp")
    )

    df = df.drop_nulls(subset=["timestamp"])

    # Keep the first occurrence of each event ID.
    df = df.unique(subset=["event_id"], keep="first", maintain_order=True)

    # Sort events chronologically.
    df = df.sort("timestamp")

    return df


def main():
    project_root = Path(__file__).resolve().parent.parent
    raw_dir = project_root / "data" / "raw"
    processed_dir = project_root / "data" / "processed"

    processed_dir.mkdir(parents=True, exist_ok=True)

    events = load_events(raw_dir)
    cleaned_df = clean_events(events)

    output_file = processed_dir / "cleaned_events.csv"
    cleaned_df.write_csv(output_file)

    print("\n--- CogniStream Processing Summary ---")
    print(f"Events loaded: {len(events)}")
    print(f"Clean events: {cleaned_df.height}")
    print(f"Rows removed: {len(events) - cleaned_df.height}")
    print(f"Output saved to: {output_file}")

    print("\nCleaned data preview:")
    print(cleaned_df.head(5))


if __name__ == "__main__":
    main()