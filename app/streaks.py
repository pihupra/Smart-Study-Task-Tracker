from rich.console import Console
from datetime import date, datetime
import json
from pathlib import Path

console = Console()
STREAK_FILE = Path("data/streaks.json")

def load_streak():
    if STREAK_FILE.exists():
        with open(STREAK_FILE, "r") as f:
            return json.load(f)
    return {"last_done": None, "streak": 0}

def save_streak(streak_data):
    with open(STREAK_FILE, "w") as f:
        json.dump(streak_data, f, indent=4)

def update_streak():
    streak_data = load_streak()
    today = date.today().isoformat()

    if streak_data["last_done"] == today:
        console.print(f"[bold green]🔥 You already completed tasks today! Streak: {streak_data['streak']}[/bold green]")
        return

    # Check if yesterday was done
    if streak_data["last_done"] == (date.today() - timedelta(days=1)).isoformat():
        streak_data["streak"] += 1
    else:
        streak_data["streak"] = 1

    streak_data["last_done"] = today
    save_streak(streak_data)
    console.print(f"[bold magenta]🔥 Your current streak is: {streak_data['streak']}[/bold magenta]")
