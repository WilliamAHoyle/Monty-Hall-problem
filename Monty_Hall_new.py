import pygame
import random
import sys


class Door:

    pygame.init()
    screen = pygame.display.set_mode((800, 200))

    goat_image = pygame.image.load("Goat.png").convert_alpha()
    door_image = pygame.image.load("Door.png").convert_alpha()
    car_image = pygame.image.load("car.png").convert_alpha()
    clicked_door = pygame.image.load('darkdoor.png').convert_alpha()

    def __init__(self, door_number, position):
        self.number = door_number
        self.image = Door.door_image
        self.rect = Door.door_image.get_rect()
        self.rect.center = position

        self.clicked = False

    def clicked_on(self):
        self.clicked = True
        self.image = Door.clicked_door

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def assign_prize(self, image, name):
        self.prize = image
        self.prize_name = name

    def open(self):
        self.image = self.prize

    def second_choice(self):
        if self.prize_name == "car":
            self.image = Door.car_image
        if self.prize_name == "goat":
            self.image = Door.goat_image


def initialize(door_list, car_image, goat_image):
    door_chosen = random.randint(0, 2)  # Index, not door number
    door_list[door_chosen].assign_prize(car_image, "car")
    copy_list = door_list[:]
    del copy_list[door_chosen]
    for item in copy_list:
        item.assign_prize(goat_image, "goat")


def monty_hall(list_of_doors):
    copy_list = list_of_doors[:]  # creates a copy list
    for element in list_of_doors:
        if element.prize_name == "car" and element.clicked:  # if you clicked on the door with the car
            chosen_door = element
            copy_list.remove(chosen_door)
            door_to_open = random.randint(0, 1)
            copy_list[door_to_open].open()
        if element.prize_name == "goat" and element.clicked:  # if you clicked on the door with a goat
            chosen_door = element
            copy_list.remove(chosen_door)
            for item in copy_list:
                if item.prize_name == "car":
                    copy_list.remove(item)
            copy_list[0].open()

def main():

    screen = pygame.display.set_mode((800, 200))

    door1 = Door(1, (200, 100))
    door2 = Door(2, (375, 100))
    door3 = Door(3, (550, 100))

    door_list = [door1, door2, door3]
    initialize(door_list, Door.car_image, Door.goat_image)

    has_monty_run = False
    is_door_chosen = False

    is_playing = True
    while is_playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_playing = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                for element in door_list:
                    if element.rect.collidepoint(x, y):
                        element.clicked_on()
                        is_door_chosen = True
            if event.type == pygame.MOUSEBUTTONDOWN and has_monty_run:
                x, y = event.pos
                for element in door_list:
                    if element.rect.collidepoint(x, y):
                        element.second_choice()

        if is_door_chosen and not has_monty_run:
            monty_hall(door_list)
            has_monty_run = True

        screen.fill(pygame.Color('gray'))

        door1.draw(screen)
        door2.draw(screen)
        door3.draw(screen)

        pygame.display.update()





    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
