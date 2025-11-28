import random
import datetime

def view_stats():
    try:
        with open("rps_history.txt", "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("No match history found yet!")
        return

    total = len(lines)
    wins = sum("YOU WIN" in line for line in lines)
    losses = sum("COMPUTER WINS" in line for line in lines)
    draws = sum("DRAW" in line for line in lines)
    quits = sum("EARLY QUIT" in line for line in lines)

    print("\n===== Your RPS Match Stats =====")
    print(f"Total matches played: {total}")
    print(f"Matches you won    : {wins}")
    print(f"Matches you lost   : {losses}")
    print(f"Drawn matches      : {draws}")
    print(f"Early quits        : {quits}")
    print("================================\n")


while True:
    print("\nRPS R.A.N.D.O.M Menu")
    print("1) Play a new match")
    print("2) View your stats")
    print("3) Quit")
    menu_choice = input("Select (1/2/3): ").strip()

    if menu_choice == "1":
        # ... the whole game code goes here! ...
        break
    elif menu_choice == "2":
        view_stats()
    elif menu_choice == "3":
        print("Bye! See you next time 🤗")
        break
    else:
        print("Invalid choice, try again!")


moves = ["rock", "paper", "scissors"]

# --- Ask for match size ("best of N") ---
while True:
    try:
        best_of = int(input("How many rounds? Only odd (3, 5, 7...): "))
        if best_of % 2 == 1 and best_of > 0:
            break
        else:
            print("Please enter a positive, odd number.")
    except ValueError:
        print("Numbers only please!")

needed_to_win = best_of // 2 + 1
player_score = 0
computer_score = 0
rounds_played = 0

print("🤖 Welcome to Rock-Paper-Scissors!")
print("Type 'quit' at any time to stop playing.")
print(f"First to {needed_to_win} wins (best of {best_of})!")
print("-" * 30)

while True:
    player_move = input("Enter rock, paper, or scissors: ").strip().lower()

    if player_move == "quit":
        print("👋 Thanks for playing!")
        print(f"🏆 FINAL SCORE -> You: {player_score} | Computer: {computer_score}")
        print(f"Total Rounds Played: {rounds_played}")
        # --- Log quit event ---
        log_line = f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S}, Best of {best_of}, Rounds: {rounds_played}, You: {player_score}, Computer: {computer_score}, Result: EARLY QUIT\n"
        with open("rps_history.txt", "a") as file:
            file.write(log_line)
        break

    if player_move not in moves:
        print("❌ Invalid move! Please check your spelling.")
        continue

    computer_move = random.choice(moves)
    print(f"You: {player_move}  VS  Computer: {computer_move}")
    
    rounds_played += 1

    if player_move == computer_move:
        print("🤝 It's a Draw!")
        # No score update
    elif (player_move == "rock" and computer_move == "scissors") or \
         (player_move == "paper" and computer_move == "rock") or \
         (player_move == "scissors" and computer_move == "paper"):
        print("🎉 You Win!")
        player_score += 1
    else:
        print("💀 Computer Wins!")
        computer_score += 1

    print(f"📊 Scoreboard: You [{player_score}] - Computer [{computer_score}]")
    print("-" * 30)

    # --- Check for end of match, log result ---
    if player_score == needed_to_win:
        print("🏆 Congrats!! You WON the match! 😎")
        log_line = f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S}, Best of {best_of}, Rounds: {rounds_played}, You: {player_score}, Computer: {computer_score}, Result: YOU WIN\n"
        with open("rps_history.txt", "a") as file:
            file.write(log_line)
        break
    elif computer_score == needed_to_win:
        print("💀 Computer wins the match. Better luck next time!")
        log_line = f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S}, Best of {best_of}, Rounds: {rounds_played}, You: {player_score}, Computer: {computer_score}, Result: COMPUTER WINS\n"
        with open("rps_history.txt", "a") as file:
            file.write(log_line)
        break


