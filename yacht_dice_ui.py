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
pygame.display.set_caption("Yacht Dice")
pygame.display.set_icon(window_icon)
dice32 = pygame.image.load("image/dice32.png")
dice64 = pygame.image.load("image/dice64.png")
dice_ace32 = pygame.image.load("image/ace32.png")
dice_deuces32 = pygame.image.load("image/deuces32.png")
dice_threes32 = pygame.image.load("image/threes32.png")
dice_fours32 = pygame.image.load("image/fours32.png")
dice_fives32 = pygame.image.load("image/fives32.png")
dice_sixes32 = pygame.image.load("image/sixes32.png")
dice_ace64 = pygame.image.load("image/ace64.png")
dice_deuces64 = pygame.image.load("image/deuces64.png")
dice_threes64 = pygame.image.load("image/threes64.png")
dice_fours64 = pygame.image.load("image/fours64.png")
dice_fives64 = pygame.image.load("image/fives64.png")
dice_sixes64 = pygame.image.load("image/sixes64.png")
choice32 = pygame.image.load("image/choice32.png")
fourofakind32 = pygame.image.load("image/quads32.png")
fullhouse32 = pygame.image.load("image/fullhouse32.png")
sstraight32 = pygame.image.load("image/sstraight32.png")
lstraight32 = pygame.image.load("image/lstraight32.png")
yacht32 = pygame.image.load("image/yacht32.png")


font_obj16 = pygame.font.Font("font/fff-forward/FFFFORWA.TTF", 16)
font_obj18 = pygame.font.Font("font/fff-forward/FFFFORWA.TTF", 18)
font_obj24 = pygame.font.Font("font/fff-forward/FFFFORWA.TTF", 24)
font_obj32 = pygame.font.Font("font/fff-forward/FFFFORWA.TTF", 32)
text_title = font_obj32.render("Yacht Dice", False, WHITE)
text_total = font_obj18.render("Total", False, WHITE)
text_ace = font_obj16.render("Ace", False, WHITE)
text_deuces = font_obj16.render("Deuces", False, WHITE)
text_threes = font_obj16.render("Threes", False, WHITE)
text_fours = font_obj16.render("Fours", False, WHITE)
text_fives = font_obj16.render("Fives", False, WHITE)
text_sixes = font_obj16.render("Sixes", False, WHITE)
text_subtotal = font_obj18.render("SubTotal", False, WHITE)
text_choice = font_obj16.render("Choice", False, WHITE)
text_fourofakind = font_obj16.render("Quads", False, WHITE)
text_fullhouse = font_obj16.render("F.House", False, WHITE)
text_sstraight = font_obj16.render("S.Strght", False, WHITE)
text_lstraight = font_obj16.render("L.Strght", False, WHITE)
text_yacht = font_obj16.render("Yacht", False, WHITE)

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
        pygame.draw.line(window, WHITE, [155, 655], [155, 705], 4)
        pygame.draw.line(window, WHITE, [255, 655], [255, 705], 1)
        #pygame.draw.line(window, WHITE, [], [], 2)

        #scores width 340 height 40 
        pygame.draw.rect(window, WHITE, [15, 450, 340, 200], 2)
        pygame.draw.line(window, WHITE, [15, 490], [355, 490], 2)
        pygame.draw.line(window, WHITE, [15, 530], [355, 530], 2)
        pygame.draw.line(window, WHITE, [15, 570], [355, 570], 2)
        pygame.draw.line(window, WHITE, [15, 610], [355, 610], 2)
        pygame.draw.line(window, WHITE, [155, 450], [155, 650], 4)
        pygame.draw.line(window, WHITE, [255, 450], [255, 650], 1)
        window.blit(fourofakind32, [20, 455])
        window.blit(fullhouse32, [20, 495])
        window.blit(sstraight32, [20, 535])
        window.blit(lstraight32, [20, 575])
        window.blit(yacht32, [20, 615])
        window.blit(text_fourofakind, [65, 460])
        window.blit(text_fullhouse, [65, 500])
        window.blit(text_sstraight, [65, 540])
        window.blit(text_lstraight, [65, 580])
        window.blit(text_yacht, [65, 620])

        #choice score 340 40
        pygame.draw.rect(window,WHITE, [15, 405, 340, 40], 2)
        pygame.draw.line(window, WHITE, [155, 405], [155, 445], 4)
        pygame.draw.line(window, WHITE, [255, 405], [255, 445], 1)
        window.blit(choice32, [20, 410])
        window.blit(text_choice, [65, 415])

        #score ace to sixes 340, 300
        pygame.draw.rect(window, WHITE, [15, 100, 340, 300], 2)
        pygame.draw.line(window, WHITE, [15, 140], [355, 140], 2)
        pygame.draw.line(window, WHITE, [15, 180], [355, 180], 2)
        pygame.draw.line(window, WHITE, [15, 220], [355, 220], 2)
        pygame.draw.line(window, WHITE, [15, 260], [355, 260], 2)
        pygame.draw.line(window, WHITE, [15, 300], [355, 300], 2)
        pygame.draw.line(window, WHITE, [15, 340], [355, 340], 2)
        pygame.draw.line(window, WHITE, [155, 365], [355, 365], 1)
        pygame.draw.line(window, WHITE, [155, 100], [155, 400], 4)
        pygame.draw.line(window, WHITE, [255, 100], [255, 400], 1)
        window.blit(dice_ace32, [20, 105])
        window.blit(dice_deuces32, [20, 145])
        window.blit(dice_threes32, [20, 185])
        window.blit(dice_fours32, [20, 225])
        window.blit(dice_fives32, [20, 265])
        window.blit(dice_sixes32, [20, 305])
        window.blit(text_ace, [65, 112])
        window.blit(text_deuces, [65, 152])
        window.blit(text_threes, [65, 192])
        window.blit(text_fours, [65, 232])
        window.blit(text_fives, [65, 272])
        window.blit(text_sixes, [65, 312])
        window.blit(text_subtotal, [34, 360])

        #player initial
        pygame.draw.rect(window, WHITE, [155, 40, 200, 60], 2)
        pygame.draw.line(window, WHITE, [255, 40], [255, 100], 2)

        window.blit(text_title, [385, 35])
        window.blit(text_total, [53, 670])

        pygame.display.update()
        fps_clock.tick(30)

    pygame.quit()

main()