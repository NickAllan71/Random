import pygame

from Cell import Direction
from Point import Point


class Player:
    def __init__(self, maze, location):
        #maze.offset = location
        self.maze = maze
        self.point = Point(location)
        self.colour = pygame.Color("yellow")
        self.direction = Direction.UP

    def update(self):
        pointlist = []
        for coordinate in self.__get_points():
            point = Point(coordinate)
            point = Point(point.offset(self.point.location))
            point = Point(point.rotate_and_scale(self.point.offset((0.5, 0.5)), self.direction.angle_in_radians, 1))
            pointlist.append(point.rotate_and_scale(self.maze.origin, self.maze.angle_in_radians, self.maze.scale_factor))

        pygame.draw.polygon(self.maze.display, self.colour, pointlist)

    @staticmethod
    def __get_points():
        return (
            (.3, .9),
            (.5, .1),
            (.7, .9)
        )

    def handle(self, event):
        if event.type != pygame.KEYDOWN:
            return

        if event.key == pygame.K_UP:
            self.__move_if_possible(self.direction)
            return

        if event.key == pygame.K_DOWN:
            self.__move_if_possible(self.direction.opposite)
            return

        if event.key == pygame.K_LEFT:
            self.direction = self.direction.rotate_anticlockwise()
        elif event.key == pygame.K_RIGHT:
            self.direction = self.direction.rotate_clockwise()

    def __move_if_possible(self, direction):
        current_cell = self.maze.cells[self.point.location]
        if direction not in current_cell.exits:
            return

        #self.maze.offset = self.point.location
        self.point.move(direction)
