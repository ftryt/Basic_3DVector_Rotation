import math
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
