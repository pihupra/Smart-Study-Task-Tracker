from rich.console import Console
from rich.prompt import Prompt
from app import tasks, streaks, game

console = Console()

def main():
    console.print("[bold underline cyan]\n📚 Smart Study/Task Tracker[/bold underline cyan]\n")

    while True:
        console.print("\n[bold yellow]Menu[/bold yellow]")
        console.print("1. Show Tasks")
        console.print("2. Add Task")
        console.print("3. Mark Daily Streak")
        console.print("4. Mini Game Break")
        console.print("5. Exit")

        choice = Prompt.ask("\nEnter your choice", choices=["1","2","3","4","5"])

        if choice == "1":
            tasks.show_tasks()
        elif choice == "2":
            tasks.add_task()
        elif choice == "3":
            streaks.update_streak()
        elif choice == "4":
            game.mini_game()
        elif choice == "5":
            console.print("[bold magenta]Goodbye! Keep being productive![/bold magenta]")
            break

if __name__ == "__main__":
    main()
