# https://leetcode.com/problems/design-snake-game/
from typing import List


class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.width = width
        self.height = height
        self.grid = [[0] * width] * height
        self.food = food
        self.food_eaten = 0
        self.position = [0, 0]

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down
        @return The game's score after the move. Return -1 if game over.
        Game over when snake crosses the screen boundary or bites its body.
        """
        if direction == "U":
            self.position[0] += 1
        elif direction == "D":
            self.position[0] -= 1
        elif direction == "R":
            self.position[1] += 1
        elif direction == "L":
            self.position[1] -= 1

        x, y = self.position
        if not (0 < x < self.width and 0 < y < self.height):
            return -1
        food = self.food[0]
        if [x, y] == food:
            self.food.pop(0)
            self.food_eaten += 1
            return self.food_eaten
        return 0