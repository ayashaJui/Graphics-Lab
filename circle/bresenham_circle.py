import matplotlib.pyplot as plt

bresenham_x1 = []
bresenham_y1 = []

bresenham_x2 = []
bresenham_y2 = []


def circle(x, y):
    bresenham_x1.append(x)
    bresenham_y1.append(y)

    bresenham_x2.append(-x)
    bresenham_y2.append(-y)


radius = int(input('Enter radius value: '))

x = 0
y = radius
d = 3 - (2 * radius)

while x <= y:
    circle(x, y)

    if d < 0:
        d = d + (4 * x) + 6
    else:
        d = d + (4 * (x - y)) + 10
        y -= 1
    x += 1

plt.figure("Bresenham Circle Drawing Algorithm")

plt.plot(bresenham_x1, bresenham_y1, color='black')
plt.plot(bresenham_y1, bresenham_x1, color='black')
plt.plot(bresenham_y2, bresenham_x1, color='black')
plt.plot(bresenham_x2, bresenham_y1, color='black')
plt.plot(bresenham_x2, bresenham_y2, color='black')
plt.plot(bresenham_y2, bresenham_x2, color='black')
plt.plot(bresenham_y1, bresenham_x2, color='black')
plt.plot(bresenham_x1, bresenham_y2, color='black')

plt.axis('square')
plt.show()
