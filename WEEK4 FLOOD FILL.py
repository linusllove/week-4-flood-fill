# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1k4YzdupbTeO3NfZbYo7k686qhDhNzHtq
"""

def flood_fill(input_board, old, new, x, y):
    if x < 0 or x >= len(input_board) or y < 0 or y >= len(input_board[0]):
        return input_board

    if input_board[x][y] == old:

        input_board[x] = input_board[x][:y] + new + input_board[x][y + 1:]

        flood_fill(input_board, old, new, x + 1, y)  # Down
        flood_fill(input_board, old, new, x - 1, y)  # Up
        flood_fill(input_board, old, new, x, y + 1)  # Right
        flood_fill(input_board, old, new, x, y - 1)  # Left

    return input_board

board = [
    "......................",
    "......##########......",
    "......#........#......",
    "......#........#......",
    "......#........#####..",
    "....###............#..",
    "....#............###..",
    "....##############....",
]

new_board = flood_fill(board, '.', 'X', 2, 11)

for row in new_board:
    print(row)
#works well
