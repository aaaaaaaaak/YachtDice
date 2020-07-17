import sys
import pygame
import yacht_dice as yd

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
window_icon = pygame.image.load("image/logo32.png")
pygame.display.set_caption("Yacht Dice")
pygame.display.set_icon(window_icon)
font_obj = pygame.font.Font("font/fff-forward/FFFFORWA.TTF", 32)
text_title = font_obj.render("Yacht Dice", False, WHITE)

fps_clock = pygame.time.Clock()


def main():
    while True:
        window.fill(BLACK)

        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            break

        pygame.draw.rect(window, WHITE, [10, 10, 350, 700], 2)
        pygame.draw.line(window, WHITE, [5, 125], [10, 125], 2)
        pygame.draw.line(window, WHITE, [360, 125], [1275, 125], 2)
        pygame.draw.rect(window, WHITE, [370, 135, 900, 575], 2)
        window.blit(text_title, [385, 20])
    
        pygame.display.update()
        fps_clock.tick(30)
        
    pygame.quit()

main()