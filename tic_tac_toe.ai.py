import random

# Function to display the Tic-Tac-Toe board
def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Function for Algorithm 1: Basic rule-based logic (play first available spot)
def basic_ai(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                return i, j

# Function for Algorithm 2: Optimized rule-based logic (win/block strategy)
def optimized_ai(board, player, opponent):
    # Check for winning move
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = player
                if check_winner(board, player):
                    board[i][j] = " "
                    return i, j
                board[i][j] = " "
    
    # Check for blocking move
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = opponent
                if check_winner(board, opponent):
                    board[i][j] = " "
                    return i, j
                board[i][j] = " "
    
    # Fallback to first available spot
    return basic_ai(board)

# Function to check for a winner
def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):  # Row
            return True
        if all(board[j][i] == player for j in range(3)):  # Column
            return True
    if all(board[i][i] == player for i in range(3)):  # Main diagonal
        return True
    if all(board[i][2 - i] == player for i in range(3)):  # Opposite diagonal
        return True
    return False

# Function to simulate a game between two algorithms
def simulate_game(alg1, alg2):
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0
    
    while " " in [cell for row in board for cell in row]:
        player = players[turn % 2]
        if turn % 2 == 0:
            move = alg1(board)  # Player X uses Algorithm 1
        else:
            move = alg2(board, "O", "X")  # Player O uses Algorithm 2, with "X" as the opponent
        board[move[0]][move[1]] = player
        if check_winner(board, player):
            return player  # Return the winner
        turn += 1
    
    return "Draw"  # If no winner, return Draw

# Simulating multiple games to compare performance
results = {"Basic AI Wins": 0, "Optimized AI Wins": 0, "Draws": 0}
for _ in range(100):  # Simulate 100 games
    winner = simulate_game(basic_ai, optimized_ai)
    if winner == "X":
        results["Basic AI Wins"] += 1
    elif winner == "O":
        results["Optimized AI Wins"] += 1
    else:
        results["Draws"] += 1

print(results)
