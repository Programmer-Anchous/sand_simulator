import pygame

from pixels import *
from vars import *


screen = pygame.display.set_mode(W_SIZE)
display = pygame.Surface((WIDTH // PIXEL_SCALE, HEIGHT // PIXEL_SCALE))
clock = pygame.time.Clock()

pixels = Pixels(display, 3)
for i in range(1, 100):
    pixels.add((i + 50, 80), "block")
pixels.add((51, 79), "block")
pixels.add((149, 79), "block")
pixels.add((100, 30), "sand")
pixels.add((100, 40), "block")


def main() -> None:
    pressed = False
    running = True
    while running:
        display.fill(BLACK)

        mx, my = pygame.mouse.get_pos()
        mx //= PIXEL_SCALE
        my //= PIXEL_SCALE

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pressed = True

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    pressed = False

        if pressed:
            pixels.add((mx, my), "sand")

        pixels.update()
        pixels.draw()

        screen.blit(pygame.transform.scale(display, W_SIZE), (0, 0))
        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
