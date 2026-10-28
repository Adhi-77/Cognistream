import json
from datetime import datetime, timedelta, timezone
from pathlib import Path


def generate_mock_events():
    now = datetime.now(timezone.utc)

    return [
        {
            "event_id": "vscode_001",
            "source": "vscode",
            "event_type": "session_start",
            "developer_id": "dev_001",
            "project": "cognistream-demo",
            "timestamp": (now - timedelta(hours=2)).isoformat(),
        },
        {
            "event_id": "vscode_002",
            "source": "vscode",
            "event_type": "file_edit",
            "developer_id": "dev_001",
            "project": "cognistream-demo",
            "timestamp": (now - timedelta(minutes=90)).isoformat(),
        },
        {
            "event_id": "vscode_003",
            "source": "vscode",
            "event_type": "session_end",
            "developer_id": "dev_001",
            "project": "cognistream-demo",
            "timestamp": (now - timedelta(minutes=60)).isoformat(),
        },
    ]


def save_events(events):
    project_root = Path(__file__).resolve().parent.parent
    output_dir = project_root / "data" / "raw"
    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / "vscode_events.json"

    with output_file.open("w", encoding="utf-8") as file:
        json.dump(events, file, indent=4)

    print(f"Saved {len(events)} mock events to: {output_file}")


if __name__ == "__main__":
    save_events(generate_mock_events())