import numpy as np
import pandas as pd
import random

class snake_game():
    def __init__(self, size_x = 10, size_y = 10) -> None:
        self.board = np.array([[' ' for x in range(size_x)] for y in range(size_y)], str)
        self.snake = [[int(size_y/2) , int(size_x/2)]]
        self.direction = '_'
        self.gen_food()
        self.score = 0

    def load_board(self, snake, food, size_x, size_y, score):
        self.size_x = size_x
        self.size_y = size_y
        self.snake = snake
        self.board = np.array([[' ' for x in range(size_x)] for y in range(size_y)], str)
        self.board[self.snake[0][0], self.snake[0][1]] = 'H'
        for i in self.snake[1:]:
            if self.board[i[0], i[1]] != ' ':
                raise 'Board Collision'
            self.board[i[0], i[1]] = 'T'
        if self.board[food[1], food[0]] != ' ':
            raise 'Board Collision'
        else:
            self.board[food[1], food[0]] = 'F'
        self.score = 0
        return

    def save_board(self):
        return
        
    def display_board(self):
        for i in self.board:
            print(i)
        return

    def gen_food(self):
        x = random.randint(0, self.size_x)
        y = random.randint(0, self.size_y)
        while self.board[y, x] != ' ':
            x = random.randint(0, self.size_x)
            y = random.randint(0, self.size_y)
        self.board[y, x] = 'F'
        self.food = [y, x]
        self.score += 1
        return
    
    def update_board(self):
        if not self.validate_snake():
            self.end_game()
        self.board[self.snake[0][0], self.snake[0][1]] == 'H'
        for i in self.snake[1:]:
            self.board[i[0], i[1]] = 'T'
        if self.food == [-1, -1]:
            self.gen_food()
        return

    def move(self, move):
        if move == 'Up':
            self.snake.insert(0, [self.snake[0][0] - 1, self.snake[0][1]])
        elif move == 'Down':
            self.snake.insert(0, [self.snake[0][0] + 1, self.snake[0][1]])
        elif move == 'Left':
            self.snake.insert(0, [self.snake[0][0], self.snake[0][1]] - 1)
        elif move == 'Right':
            self.snake.insert(0, [self.snake[0][0], self.snake[0][1]] + 1)
        self.validate_snake(self)
        if self.board[self.snake[0][0], self.snake[0][1]] == 'F':
            self.eat_food()
        else:
            self.board[self.snake[-1][0], self.snake[-1][1]] = ' '
            self.snake = self.snake[:-1]
        self.update_board()

    def eat_food(self):
        self.board[self.snake[0][0], self.snake[0][1]] = ' '
        self.food = [-1, -1]
        return

    def validate_snake(self):
        if self.snake[0][0] < 0 or self.snake[0][0] >= self.size_x:
            return False
        elif self.snake[0][1] < 0 or self.snake[0][1] >= self.size_y:
            return False
        if self.snake[0] in self.snake[1:]:
            return False
        return True
    
    def end_game(self):

    ##Check the move is valid
    ##Check if food is eaten
    ##Move snake image
    ##Gen food