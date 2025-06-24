import random

class YahtzeeGame:
    def __init__(self):
        self.dice = [0, 0, 0, 0, 0]
        self.held_dice = [False, False, False, False, False]
        self.turn = 1
        self.max_turns = 3
    
    def roll_dice(self):
        for i in range(5):
            if not self.held_dice[i]:
                self.dice[i] = random.randint(1, 6)
    
    def hold_dice(self, dice_indices):
        for i in range(5):
            self.held_dice[i] = i in dice_indices
    
    def display_dice(self):
        print("\nCurrent dice:")
        for i, die in enumerate(self.dice):
            hold_status = " (HELD)" if self.held_dice[i] else ""
            print(f"Die {i+1}: {die}{hold_status}")
    
    def reset_turn(self):
        self.turn = 1
        self.held_dice = [False, False, False, False, False]
    
    def play_round(self):
        print(f"\n=== YAHTZEE ROUND ===")
        self.reset_turn()
        
        while self.turn <= self.max_turns:
            print(f"\n--- Turn {self.turn} of {self.max_turns} ---")
            
            if self.turn == 1:
                print("Rolling all dice...")
            else:
                print("Rolling non-held dice...")
            
            self.roll_dice()
            self.display_dice()
            
            if self.turn < self.max_turns:
                print("\nWhich dice would you like to HOLD for the next roll?")
                print("Enter dice numbers (1-5) separated by spaces, or press Enter to hold none:")
                
                try:
                    user_input = input("> ").strip()
                    if user_input:
                        dice_to_hold = [int(x) - 1 for x in user_input.split() if 1 <= int(x) <= 5]
                        self.hold_dice(dice_to_hold)
                        
                        if dice_to_hold:
                            held_names = [str(i+1) for i in dice_to_hold]
                            print(f"Holding dice: {', '.join(held_names)}")
                    else:
                        self.hold_dice([])
                        print("Not holding any dice")
                        
                except ValueError:
                    print("Invalid input. Not holding any dice.")
                    self.hold_dice([])
            
            self.turn += 1
        
        print(f"\n=== FINAL RESULT ===")
        print("Final dice values:")
        for i, die in enumerate(self.dice):
            print(f"Die {i+1}: {die}")
        
        print(f"\nDice sorted: {sorted(self.dice)}")
        
        play_again = input("\nPlay another round? (y/n): ").lower().strip()
        if play_again == 'y':
            self.play_round()
        else:
            print("Thanks for playing Yahtzee!")

def main():
    print("Welcome to Yahtzee!")
    print("Rules: Roll 5 dice, then choose which to hold between rolls.")
    print("You get 3 rolls total per round.")
    
    game = YahtzeeGame()
    game.play_round()

if __name__ == "__main__":
    main()