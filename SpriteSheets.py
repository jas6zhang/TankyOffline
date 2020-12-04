import pygame

BLACK = (0,0,0)

## Made by programarcadegames.com

## Used to seperate sprites on a sprite sheet 
class SpriteSheet(object):
 
    def __init__(self, file_name):
 
        # Load the sprite sheet.
        self.sprite_sheet = pygame.image.load(file_name).convert()
 
 
    def get_image(self, x, y, width, height):

        # Create a new blank image
        image = pygame.Surface([width, height]).convert()
 
        # Copy the sprite from the large sheet onto the smaller image
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
 
        # Assuming black works as the transparent color
        image.set_colorkey(BLACK,0)
 
        # Return the image
        return image