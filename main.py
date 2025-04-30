from random import choice
from colorama import Fore, Style, init
from typing import Optional
from dataclasses import dataclass

# Initialize colorama
init(autoreset=True)

@dataclass
class GameState:
    current_province: str
    target_province: str
    moves: int = 0

class ProvinceGame:
    DIRECTIONS = ["norr", "nordöst", "öster", "sydöst", "söder", "sydväst", "väst", "nordväst"]
    
    def __init__(self, provinces: dict):
        self.provinces = provinces
        self.state = self._initialize_game()

    def _initialize_game(self) -> GameState:
        """Initialize a new game with random start and target provinces."""
        all_provinces = list(self.provinces.keys())
        start = choice(all_provinces)
        target = choice([p for p in all_provinces if p != start])
        return GameState(start, target)

    def get_valid_moves(self) -> list[str]:
        """Return list of valid directions from current province."""
        return [dir for dir in self.DIRECTIONS 
                if dir in self.provinces[self.state.current_province]]

    def move(self, direction: str) -> tuple[bool, str]:
        """
        Attempt to move in the given direction.
        Returns: (success, message)
        """
        if direction not in self.DIRECTIONS:
            return False, "Ogiltig riktning. Försök igen."

        next_province = self.provinces[self.state.current_province].get(direction)
        if not next_province:
            return False, f"Det finns ingen provins {direction} om {self.state.current_province}."

        self.state.current_province = next_province
        self.state.moves += 1
        return True, f"Du går {direction} till {next_province}."

    def is_complete(self) -> bool:
        """Check if player has reached the target province."""
        return self.state.current_province == self.state.target_province

    def get_status(self) -> str:
        """Get current game status message."""
        return (f"Du är i {self.state.current_province}.\n"
                f"Ditt mål är att nå {self.state.target_province}.\n"
                f"Giltiga riktningar: {', '.join(self.get_valid_moves())}")

def main():
    # Exempel på provinces dictionary
    provinces = {
        "Stockholm": {
            "norr": "Uppsala",
            "väst": "Västerås",
            "söder": "Södertälje"
        },
        "Uppsala": {
            "söder": "Stockholm",
            "väst": "Västerås"
        },
        "Västerås": {
            "öst": "Stockholm",
            "nordöst": "Uppsala"
        },
        "Södertälje": {
            "norr": "Stockholm"
        }
    }
    
    game = ProvinceGame(provinces)
    print(Fore.GREEN + "Välkommen till Provinces-spelet!")
    
    while True:
        print(Fore.CYAN + game.get_status())
        
        direction = input("Vilken riktning vill du gå? ").lower()
        success, message = game.move(direction)
        
        print(Fore.RED + message if not success else Fore.GREEN + message)
        
        if game.is_complete():
            print(Fore.YELLOW + 
                f"Grattis! Du nådde {game.state.target_province} på {game.state.moves} drag!")
            break

if __name__ == "__main__":
    main()