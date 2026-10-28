import json
from datetime import datetime, timedelta, timezone
from pathlib import Path


def generate_mock_events():
    """Generate sample GitHub-style events for pipeline testing."""
    now = datetime.now(timezone.utc)

    return [
        {
            "event_id": "gh_001",
            "source": "github",
            "event_type": "commit",
            "developer_id": "dev_001",
            "repository": "cognistream-demo",
            "timestamp": (now - timedelta(hours=3)).isoformat(),
        },
        {
            "event_id": "gh_002",
            "source": "github",
            "event_type": "pull_request",
            "developer_id": "dev_001",
            "repository": "cognistream-demo",
            "timestamp": (now - timedelta(hours=2)).isoformat(),
        },
        {
            "event_id": "gh_003",
            "source": "github",
            "event_type": "issue",
            "developer_id": "dev_002",
            "repository": "cognistream-demo",
            "timestamp": (now - timedelta(hours=1)).isoformat(),
        },
    ]


def save_events(events):
    """Save mock events as JSON in data/raw."""
    project_root = Path(__file__).resolve().parent.parent
    output_dir = project_root / "data" / "raw"
    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / "github_events.json"

    with output_file.open("w", encoding="utf-8") as file:
        json.dump(events, file, indent=4)

    print(f"Saved {len(events)} mock events to: {output_file}")


if __name__ == "__main__":
    events = generate_mock_events()
    save_events(events)