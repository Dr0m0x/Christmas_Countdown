import time
from datetime import datetime
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
import os
import pygame

# Initialize console for colorful output
console = Console()


# Function to play music
def play_music():
    file_path = r"C:\Users\MoHol\PathToMusic\jingle_bells.mp3"

    # Check if the file exists
    if not os.path.exists(file_path):
        console.print("❌ Music file not found! Please check the file path.", style="bold red")
        return

    # Play the music
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play(-1)  # Loop indefinitely
    console.print("🎵 Playing Christmas music! 🎶", style="bold green")


# Function to calculate the countdown
def calculate_countdown():
    today = datetime.now()
    christmas_date = datetime(today.year, 12, 25, 0, 0, 0)

    # Check if Christmas has passed this year
    if today > christmas_date:
        christmas_date = datetime(today.year + 1, 12, 25, 0, 0, 0)

    countdown = christmas_date - today
    return countdown


# Function to display the countdown with fun visuals
def display_countdown():
    while True:
        countdown = calculate_countdown()

        # Extract days, hours, minutes, and seconds
        days = countdown.days
        seconds_remaining = countdown.seconds
        hours, remainder = divmod(seconds_remaining, 3600)
        minutes, seconds = divmod(remainder, 60)

        # Clear the console
        os.system('cls' if os.name == 'nt' else 'clear')

        # ASCII art for the Christmas tree
        tree = """
                 🎄
                🎄🎄
               🎄🎄🎄
              🎄🎄🎄🎄
             🎄🎄🎄🎄🎄
            🎄🎄🎄🎄🎄🎄
           🎄🎄🎄🎄🎄🎄🎄
              🎁🎁🎁
        """

        # Prepare the countdown message
        countdown_text = Text()
        countdown_text.append(f"\n🎅 Santa is on his way! 🎅\n\n", style="bold green")
        countdown_text.append(f"🎄 Days: {days}  ", style="bold cyan")
        countdown_text.append(f"⏰ Hours: {hours}  ", style="bold yellow")
        countdown_text.append(f"🎁 Minutes: {minutes}  ", style="bold magenta")
        countdown_text.append(f"⭐ Seconds: {seconds}\n", style="bold red")
        countdown_text.append("\nKeep being good, and Santa will visit soon! 🎁❄️", style="bold white")

        # Print everything
        console.print(Panel.fit(tree, title="🎄 Christmas Countdown 🎄", title_align="center", style="bold green"))
        console.print(countdown_text)

        # Add a little pause for animation effect
        time.sleep(1)


# Main function to start the program
if __name__ == "__main__":
    try:
        # Play music in the background
        play_music()

        # Start the countdown display
        display_countdown()
    except KeyboardInterrupt:
        console.print("\n🎅 See you next time! Merry Christmas! 🎄", style="bold red")
        pygame.mixer.music.stop()
