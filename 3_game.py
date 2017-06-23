import pygame


# noinspection PyGlobalUndefined
# def loadImage(filename):
#     image = pygame.image.load(filename).convert()
#     transColor = image.get_at((0, 0))
#     image.set_colorkey(transColor)


def main():

    pygame.init()
    screen = pygame.display.set_mode((800, 600))

    pygame.display.set_caption("Game-Development")
    pygame.mouse.set_visible(1)
    # noinspection PyArgumentList
    pygame.key.set_repeat(1, 30)

    clock = pygame.time.Clock()
    #loadImage("graphics/heroes/hero_dashi.png")
    running = True

    while running:
        clock.tick(30)

        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # noinspection PyArgumentList
                    pygame.event.post(pygame.event.Event(pygame.QUIT))
                if event.key == pygame.K_w:
                    print("Hallo")

        # screen.blit(image, (0, 10))
        pygame.display.flip()

if __name__ == "__main__":
    main()
