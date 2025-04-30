from random import choice
from colorama import Fore, Style, init
import Resources.StateObject as SO

# Initialize colorama
init(autoreset=True)

def get_random_province(provinces):
    """Select a random province from the dictionary."""
    return choice(list(provinces.keys()))

def get_direction_input():
    """Prompt the user for a direction input."""
    available_directions = ["norr", "nordöst", "öster", "sydöst", "söder", "sydväst", "väst", "nordväst"]
    selected_direction = input('In what direction do you want to go? \nAnswer: ').lower()
    if selected_direction in available_directions:
        return selected_direction

    return ""

def print_colored(text, color):
    """Print text in the specified color."""
    print(color + text)

def main():
    current_province = get_random_province(SO.Provinces)

    while True:
        print_colored(f"You're now standing in the province of {current_province.capitalize()}", Fore.GREEN)

        while True:
            direction = get_direction_input()
            next_province = SO.Provinces[current_province].get(direction, "")

            if next_province:
                print_colored(f"You are moving into {next_province}.", Fore.BLUE)
                current_province = next_province
                break  # Exit the inner loop if the direction is valid
            else:
                print_colored("Invalid direction or no province in that direction. Please try again.", Fore.RED)

if __name__ == "__main__":
    main()
