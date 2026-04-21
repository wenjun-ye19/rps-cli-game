import random
import time

def play():
    user = input("\nWhat's your choice? 'r' for Rock, 'p' for Paper, 's' for Scissors: ").lower()
    
    if user not in ['r', 'p', 's']:
        return "⚠️ Invalid choice! Please stick to r, p, or s."

    computer = random.choice(['r', 'p', 's'])
    options = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}
    
    print(f"\n🤖 Opponent has selected: {options[computer]}!")

    if user == computer:
        return "It's a draw! 🤝"
    
    if is_win(user, computer):
        return "You won! 🎉 You beat your opponent!"

    return "You lost! 😅 Your opponent beats you!"

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or \
       (player == 's' and opponent == 'p') or \
       (player == 'p' and opponent == 'r'):
        return True

def countdown(seconds=3):
    """Displays a real-time countdown."""
    for i in range(seconds, 0, -1):
        print(i, end='...', flush=True) # ensures immediate output
        time.sleep(1)
    print("GO!\n")

def main():
    print("👋 Hello! Welcome to the Rock, Paper, Scissors Game! 🤗")
    
    while True:
        choice = input("\nEnter 'P' to Play, 'Q' to Quit, or 'H' for Help: ").upper()
        
        if choice == 'P':
            print("\n🎮 Game starting in...")
            countdown(3) # countdown before the game starts
            result = play()
            print(f"\n>>> {result} <<<\n")
            
        elif choice == 'Q':
            print("Oh, you changed your mind? No worries! Hope to see you again soon. 👋")
            break
            
        elif choice == 'H':
            print("\n--- 📜 GUIDE ---")
            print("Rock (r)  🪨  crushes Scissors (s)  ✂️")
            print("Scissors (s)  ✂️  cuts Paper (p)  📄")
            print("Paper (p)  📄 covers Rock (r)  🪨")
            print("----------------\n")
            
        else:
            print("⚠️ Invalid choice! Try again.")

if __name__ == "__main__":
    main()