import json
from datetime import datetime, timedelta, timezone
from pathlib import Path


def generate_mock_events():
    now = datetime.now(timezone.utc)

    return [
        {
            "event_id": "slack_001",
            "source": "slack",
            "event_type": "message",
            "developer_id": "dev_001",
            "channel": "project-updates",
            "timestamp": (now - timedelta(minutes=45)).isoformat(),
        },
        {
            "event_id": "slack_002",
            "source": "slack",
            "event_type": "mention",
            "developer_id": "dev_002",
            "channel": "engineering",
            "timestamp": (now - timedelta(minutes=25)).isoformat(),
        },
        {
            "event_id": "slack_003",
            "source": "slack",
            "event_type": "notification",
            "developer_id": "dev_001",
            "channel": "project-updates",
            "timestamp": (now - timedelta(minutes=10)).isoformat(),
        },
    ]


def save_events(events):
    project_root = Path(__file__).resolve().parent.parent
    output_dir = project_root / "data" / "raw"
    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / "slack_events.json"

    with output_file.open("w", encoding="utf-8") as file:
        json.dump(events, file, indent=4)

    print(f"Saved {len(events)} mock events to: {output_file}")


if __name__ == "__main__":
    save_events(generate_mock_events())