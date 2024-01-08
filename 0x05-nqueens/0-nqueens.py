#!/usr/bin/python3
"""
python program that solves the N queens problem
It uses backtracking to find all possible solutions
"""
import sys


def solve_n_queens(n):
    def can_place(pos, ocuppied_positions):
        for i in range(len(ocuppied_positions)):
            if ocuppied_positions[i] == pos or \
                ocuppied_positions[i] - i == pos - len(ocuppied_positions) or \
                    ocuppied_positions[i] + i == pos + len(ocuppied_positions):
                return False
        return True

    def place_queens(n, index, ocuppied_positions, all_solutions):
        if index == n:
            all_solutions.append(ocuppied_positions[:])
            return

        for i in range(n):
            if can_place(i, ocuppied_positions):
                ocuppied_positions.append(i)
                place_queens(n, index + 1, ocuppied_positions, all_solutions)
                ocuppied_positions.pop()

    all_solutions = []
    place_queens(n, 0, [], all_solutions)
    return all_solutions


def print_solutions(solutions):
    for solution in solutions:
        formatted_solution = [[i, pos] for i, pos in enumerate(solution)]
        print(formatted_solution)


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_n_queens(n)
    print_solutions(solutions)


if __name__ == "__main__":
    main()
