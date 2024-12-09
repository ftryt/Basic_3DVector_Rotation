# Example file showing a basic pygame "game loop"
import pygame, math

def rotate2Dvector(vec2in, angle):
    angle = math.radians(angle)
    return pygame.Vector2(vec2in[0] * math.cos(angle) - vec2in[1] * math.sin(angle),
                          vec2in[1] * math.cos(angle) + vec2in[0] * math.sin(angle))

def rotate3Dvector(vec3in, angles):
    # Rotate (X, Y, Z)
    angles = [math.radians(i) for i in angles]
    # Rotate X
    vec3in = (vec3in[0],
              vec3in[1] * math.cos(angles[0]) + vec3in[2] * math.sin(angles[0]),
              vec3in[2] * math.cos(angles[0]) - vec3in[1] * math.sin(angles[0]))
    # Rotate Y
    vec3in = (vec3in[0] * math.cos(angles[1]) - vec3in[2] * math.sin(angles[1]),
              vec3in[1],
              vec3in[2] * math.cos(angles[1]) + vec3in[0] * math.sin(angles[1]))
    # Rotate Z
    vec3in = (vec3in[0] * math.cos(angles[2]) - vec3in[1] * math.sin(angles[2]),
              vec3in[1] * math.cos(angles[2]) + vec3in[0] * math.sin(angles[2]),
              vec3in[2])

    return vec3in

def get3DVecLen(vec3in):
    return (vec3in[0] ** 2 + vec3in[1] ** 2 + vec3in[2] ** 2) ** 0.5

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
centerVec = pygame.Vector2(1280 / 2, 720 / 2)
points = [(100, 100, -100), (-100, 100, -100), (-100, -100, -100), (100, -100, -100),
          (100, 100, 100), (-100, 100, 100), (-100, -100, 100), (100, -100, 100)]
cusWidth = 4

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    # RENDER YOUR GAME HERE

    for n, i in enumerate(points):
        pygame.draw.circle(screen, "red", centerVec + (i[0], i[1]), 5, cusWidth)
        points[n] = rotate3Dvector(i, (0, 1, 1))
    pygame.draw.lines(screen, "blue", True, [(i[0], i[1]) + centerVec for i in points[0:4]])
    pygame.draw.lines(screen, "blue", True, [(i[0], i[1]) + centerVec for i in points[4:8]])
    for i in range(4):
        pygame.draw.line(screen, "blue", (points[i][0], points[i][1]) + centerVec, (points[i+4][0], points[i+4][1]) + centerVec)

    # RENDER END

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(30)  # limits FPS to 60

pygame.quit()