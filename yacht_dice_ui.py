import sys
import pygame
import yacht_dice as yd

PLAYING = True
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
window_icon = pygame.image.load("image/logo32.png")
dice_ace = pygame.image.load("image/image64.png")
pygame.display.set_caption("Yacht Dice")
pygame.display.set_icon(window_icon)
font_obj32 = pygame.font.Font("font/fff-forward/FFFFORWA.TTF", 32)
font_obj18 = pygame.font.Font("font/fff-forward/FFFFORWA.TTF", 18)
text_title = font_obj32.render("Yacht Dice", False, WHITE)
text_total = font_obj18.render("Total", False, WHITE)

fps_clock = pygame.time.Clock()


def main():
    while True:
        window.fill(BLACK)

        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            break

        # score board
        pygame.draw.rect(window, WHITE, [10, 10, 350, 700], 2)

        # updown grid
        pygame.draw.line(window, WHITE, [5, 125], [10, 125], 2)
        pygame.draw.line(window, WHITE, [360, 125], [1275, 125], 2)
        
        # board
        pygame.draw.rect(window, WHITE, [370, 135, 900, 575], 2)

        # keep disband
        pygame.draw.rect(window, WHITE, [375, 140, 66, 66], 1)
        pygame.draw.rect(window, WHITE, [445, 140, 66, 66], 1)
        pygame.draw.rect(window, WHITE, [515, 140, 66, 66], 1)
        pygame.draw.rect(window, WHITE, [585, 140, 66, 66], 1)
        pygame.draw.rect(window, WHITE, [655, 140, 66, 66], 1)

        # total
        pygame.draw.rect(window, WHITE, [15, 655, 340, 50], 2)
        pygame.draw.line(window, WHITE, [155, 655], [155, 705], 2)
        pygame.draw.line(window, WHITE, [255, 655], [255, 705], 1)
        #pygame.draw.line(window, WHITE, [], [], 2)

        #scores width 340 height 40 
        window.blit(text_title, [385, 35])
        window.blit(text_total, [55, 670])

        pygame.display.update()
        fps_clock.tick(30)

    pygame.quit()

main()