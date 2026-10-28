import json
from datetime import datetime, timedelta, timezone
from pathlib import Path


def generate_mock_events():
    now = datetime.now(timezone.utc)

    return [
        {
            "event_id": "jira_001",
            "source": "jira",
            "event_type": "issue_created",
            "developer_id": "dev_001",
            "issue_key": "COG-101",
            "timestamp": (now - timedelta(hours=4)).isoformat(),
        },
        {
            "event_id": "jira_002",
            "source": "jira",
            "event_type": "issue_updated",
            "developer_id": "dev_002",
            "issue_key": "COG-102",
            "timestamp": (now - timedelta(hours=2)).isoformat(),
        },
        {
            "event_id": "jira_003",
            "source": "jira",
            "event_type": "issue_completed",
            "developer_id": "dev_001",
            "issue_key": "COG-101",
            "timestamp": (now - timedelta(minutes=30)).isoformat(),
        },
    ]


def save_events(events):
    project_root = Path(__file__).resolve().parent.parent
    output_dir = project_root / "data" / "raw"
    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / "jira_events.json"

    with output_file.open("w", encoding="utf-8") as file:
        json.dump(events, file, indent=4)

    print(f"Saved {len(events)} mock events to: {output_file}")


if __name__ == "__main__":
    save_events(generate_mock_events())