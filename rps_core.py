import random
import datetime

MOVES = ["rock", "paper", "scissors"]

def play_round(player_move):
    computer_move = random.choice(MOVES)
    if player_move == computer_move:
        result = "draw"
    elif (player_move == "rock" and computer_move == "scissors") or \
         (player_move == "paper" and computer_move == "rock") or \
         (player_move == "scissors" and computer_move == "paper"):
        result = "win"
    else:
        result = "lose"
    return computer_move, result

def log_match(best_of, rounds_played, player_score, computer_score, result):
    log_line = (
        f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S}, "
        f"Best of {best_of}, Rounds: {rounds_played}, You: {player_score}, Computer: {computer_score}, Result: {result.upper()}\n"
    )
    with open("rps_history.txt", "a") as file:
        file.write(log_line)
