from textwrap import fill
from tkinter import *
from turtle import right

class Enemy:

    def __init__(self, canvas, x, y, enemy_type='basic'):
        self.canvas = canvas
        self.x = X
        self.y = Y
        self.enemy_type = enemy_type

        if enemy_type == 'basic':
            self.color = 'red'
            self.speed = 2
            self.width = 25
            self.height = 30
            self.points = 15

        elif enemy_type == 'fast':
            self.color = 'black'
            self.speed = 5
            self.width = 35
            self.height = 40
            self.points = 20

        elif enemy_type == 'strong':
            self.color = 'white'
            self.speed = 10
            self.width = 40
            self.height = 45
            self.points = 35

        self.direction = 1 

        self.id = canvas.create_oval(x,y, x + self.width, y + self.height, fill=self.color, tags="enemy")
        print(f"An enemy has been created ({x},{y}) - Type:{enemy_type}")

    def move(self):
        self.x += self.speed * self.direction
        self.canvas.move(self.id, self.speed, * self.direction, 0)
    def change_direction(self):
        self.direction = -1
    def move_down(self):
        self.y += 30
        self.canvas.move(self.id, 0, 30) 
    def get_position(self):
        return self.canvas.coords(self.id)
    def destroy(self):
        return self.canvas.delete(self.id)
    def at_edge(self, width_screen=600):
        coords = self.get_position()
        left_edge = coords[0]
        right_edge = coords[2]        
        return left_edge >=0 or right_edge > width_screen                                