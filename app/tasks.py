import json
from pathlib import Path
from rich.console import Console
from rich.table import Table
from rich.progress import Progress

console = Console()
TASK_FILE = Path("data/tasks.json")
TASK_FILE.parent.mkdir(exist_ok=True)

# Load tasks
def load_tasks():
    if TASK_FILE.exists():
        with open(TASK_FILE, "r") as f:
            return json.load(f)
    return []

# Save tasks
def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

# Add task
def add_task():
    task_name = console.input("[bold cyan]Enter task name: [/bold cyan]")
    priority = console.input("[green]Enter priority (High/Medium/Low): [/green]")
    deadline = console.input("[yellow]Enter deadline (YYYY-MM-DD): [/yellow]")

    tasks = load_tasks()
    tasks.append({
        "name": task_name,
        "priority": priority,
        "deadline": deadline,
        "done": False
    })
    save_tasks(tasks)
    console.print("[bold green]✅ Task added successfully![/bold green]")

# Show tasks with progress bars
def show_tasks():
    tasks = load_tasks()
    if not tasks:
        console.print("[italic]No tasks added yet.[/italic]")
        return
    
    table = Table(title="📋 Your Tasks")
    table.add_column("Name", style="bold cyan")
    table.add_column("Priority", style="green")
    table.add_column("Deadline", style="yellow")
    table.add_column("Status", style="magenta")

    completed = 0
    for t in tasks:
        status = "[green]Done[/green]" if t["done"] else "[red]Pending[/red]"
        if t["done"]:
            completed += 1
        table.add_row(t["name"], t["priority"], t["deadline"], status)
    
    console.print(table)

    # Show progress bar for tasks
    total = len(tasks)
    if total > 0:
        with Progress() as progress:
            task = progress.add_task("[cyan]Task Completion...", total=total)
            progress.update(task, completed=completed)
