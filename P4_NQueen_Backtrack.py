# Implement a solution for a Constraint Satisfaction Problem using Branch and Bound andBacktracking for n-queens problem or a graph coloring problem.

N = int(input("Enter the number of queens: "))
board = [[0] * N for _ in range(N)]

def is_attack(row, col):
    for i in range(N):
        if board[row][i] == 1 or board[i][col] == 1:
            return True
    for i in range(N):
        for j in range(N):
            if abs(row - i) == abs(col - j) and board[i][j] == 1:
                return True
    return False

def solve_n_queens(n):
    if n == 0:
        return True
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0 and not is_attack(i, j):
                board[i][j] = 1
                if solve_n_queens(n - 1):
                    return True
                board[i][j] = 0
    return False

if solve_n_queens(N):
    print("Solution for the N-Queens Problem:")
    for row in board:
        print(row)
else:
    print("No solution exists.")


# The code solves the N-Queens problem, where the task is to place N queens on an N x N chessboard such that no two queens attack each other.

# It first takes the number of queens (`N`) as input.
# Then, it creates an empty chessboard of size `N x N`.
# The `is_attack()` function checks if placing a queen at a specific position would result in an attack.
# The `solve_n_queens()` function uses **backtracking** to try placing queens one by one:
# It places a queen in an empty spot, then recursively tries to place the next queen.
# If a valid arrangement is found, it prints the board. If not, it backtracks and tries a different arrangement.
#  The program outputs the solution if one exists or says "No solution exists."
