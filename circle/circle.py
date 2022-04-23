import matplotlib.pyplot as plt

bresenham_x1 = []
bresenham_y1 = []

bresenham_x2 = []
bresenham_y2 = []

midpoint_x1 = []
midpoint_y1 = []

midpoint_x2 = []
midpoint_y2 = []


def circle(x, y, name):
    if name == 'bresenham':
        bresenham_x1.append(x)
        bresenham_y1.append(y)

        bresenham_x2.append(-x)
        bresenham_y2.append(-y)
    elif name == 'midpoint':
        midpoint_x1.append(x)
        midpoint_y1.append(y)

        midpoint_x2.append(-x)
        midpoint_y2.append(-y)


def bresenham(r):
    x = 0
    y = r
    d = 3 - (2 * r)

    while x <= y:
        circle(x, y, "bresenham")

        if d < 0:
            d = d + (4 * x) + 6
        else:
            d = d + (4 * (x - y)) + 10
            y -= 1
        x += 1


def midpoint(r):
    x = 0
    y = r
    p = 1 - r

    while x <= y:
        circle(x, y, "midpoint")

        if p < 0:
            p = p + (2 * x) + 3
        else:
            p = p + (2 * (x - y)) + 5
            y -= 1
        x += 1


radius = int(input('Enter radius value: '))

bresenham(radius)
midpoint(radius)

plt.figure("Circle Drawing Algorithm")
plt.plot(bresenham_x1, bresenham_y1, color='black', label="Bresenham")
plt.plot(bresenham_y1, bresenham_x1, color='black')
plt.plot(bresenham_y2, bresenham_x1, color='black')
plt.plot(bresenham_x2, bresenham_y1, color='black')
plt.plot(bresenham_x2, bresenham_y2, color='black')
plt.plot(bresenham_y2, bresenham_x2, color='black')
plt.plot(bresenham_y1, bresenham_x2, color='black')
plt.plot(bresenham_x1, bresenham_y2, color='black')

plt.plot(midpoint_x1, midpoint_y1, color='orange', label="Midpoint", linestyle='--')
plt.plot(midpoint_y1, midpoint_x1, color='orange', linestyle='--')
plt.plot(midpoint_y2, midpoint_x1, color='orange', linestyle='--')
plt.plot(midpoint_x2, midpoint_y1, color='orange', linestyle='--')
plt.plot(midpoint_x2, midpoint_y2, color='orange', linestyle='--')
plt.plot(midpoint_y2, midpoint_x2, color='orange', linestyle='--')
plt.plot(midpoint_y1, midpoint_x2, color='orange', linestyle='--')
plt.plot(midpoint_x1, midpoint_y2, color='orange', linestyle='--')

plt.axis('square')
plt.legend()
plt.show()
