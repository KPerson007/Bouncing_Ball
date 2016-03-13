import sys, pygame
pygame.init()

size = width, height = 320, 240
speed = [1, 1]
skips = 50
black = 255, 255, 255

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Bouncing Ball")

ball = pygame.image.load("ball.bmp")
pygame.display.set_icon(ball)
ballrect = ball.get_rect()

i = 0
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            (x, y) = pygame.mouse.get_pos()
            ballrect.x = x
            ballrect.y = y
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: #decrease horizontal speed
                if speed[0] < 0:
                    speed[0] = speed[0] + 1
                elif speed[0] > 0:
                    speed[0] = speed[0] - 1
            if event.key == pygame.K_RIGHT: #increase horizontal speed
                if speed[0] < 0:
                    speed[0] = speed[0] - 1
                elif speed[0] >= 0:
                    speed[0] = speed[0] + 1
            if event.key == pygame.K_UP: #increase vertical speed
                if speed[1] <= 0:
                    speed[1] = speed[1] - 1
                elif speed[1] > 0:
                    speed[1] = speed[1] + 1
            if event.key == pygame.K_DOWN: #decrease vertical speed
                if speed[1] < 0:
                    speed[1] = speed[1] + 1
                elif speed[1] > 0:
                    speed[1] = speed[1] - 1
            if event.key == pygame.K_0 or event.key == pygame.K_KP0: #set speed to 0
                speed[0] = 0
                speed[1] = 0

    if (ballrect.left < 0 or ballrect.right > width) and i == skips:
        speed[0] = -speed[0]
    if (ballrect.top < 0 or ballrect.bottom > height) and i == skips:
        speed[1] = -speed[1]
    if i == skips:
        ballrect = ballrect.move(speed)
        i = 0

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
    i = i + 1