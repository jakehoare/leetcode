_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/design-snake-game/
# Design a Snake game that is played on a device with screen size = width x height.
# The snake is initially positioned at the top left corner (0,0) with length = 1 unit.
# You are given a list of food's positions in row-column order. When a snake eats the food, its length and the game's
# score both increase by 1.  Each food appears one by one on the screen. For example, the second food will not appear
# until the first food was eaten by the snake.  When a food does appear on the screen, it is guaranteed that it will not
# appear on a block occupied by the snake.

# Dictionary maps one segment of snake body to the next.  Check for collision with wall or body apart from tail.
# Score is len(snake) - 1.
# Time - O(f) for constructor (nb food), O(1) to move()
# Space - O(n)

class SnakeGame(object):

    def __init__(self, width,height,food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        self.rows, self.cols = height, width
        self.food = [tuple(f) for f in food]    # convert to tuples
        self.snake = {(0, 0) : None}            # map from position to next position
        self.head, self.tail = (0, 0), (0, 0)
        self.moves = {"U" : (-1, 0), "D" : (1, 0), "L" : (0, -1), "R" : (0, 1)}

    def move(self, direction):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down
        @return The game's score after the move. Return -1 if game over.
        Game over when snake crosses the screen boundary or bites its body.
        :type direction: str
        :rtype: int
        """
        # get new head position
        new_head = (self.head[0] + self.moves[direction][0], self.head[1] + self.moves[direction][1])

        # check collision with wall
        if new_head[0] < 0 or new_head[0] >= self.rows or new_head[1] < 0 or new_head[1] >= self.cols:
            return -1
        # check if hits body (apart from tail which will move or not be hit since eating food)
        if new_head in self.snake and new_head != self.tail:
            return -1

        # update head
        self.snake[self.head] = new_head
        self.head = new_head

        # move tail if not eaten food
        if len(self.snake) - 1 >= len(self.food) or new_head != self.food[len(self.snake) - 1]:
            old_tail = self.tail
            self.tail = self.snake[self.tail]
            del self.snake[old_tail]    # head has moved on fo safe even if length 1

        # extend length
        self.snake[self.head] = None

        return len(self.snake) - 1
