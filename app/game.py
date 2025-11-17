import random
from rich.console import Console
from rich.prompt import Prompt

console = Console()

def mini_game():
    console.print("\n[bold magenta]🎮 Mini Game Break! Guess the Number[/bold magenta]")
    console.print("[cyan]Guess the number between 1 and 20 to relax for a bit![/cyan]")

    number = random.randint(1, 20)
    guess = 0
    attempts = 0

    while guess != number:
        guess = int(Prompt.ask("Enter your guess"))
        attempts += 1
        if guess < number:
            console.print("[yellow]Too low![/yellow]")
        elif guess > number:
            console.print("[yellow]Too high![/yellow]")
        else:
            console.print(f"[bold green]🎉 Correct! You guessed it in {attempts} tries![/bold green]")
            break
