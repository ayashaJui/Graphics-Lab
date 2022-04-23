import matplotlib.pyplot as plt

midpoint_x1 = []
midpoint_y1 = []

midpoint_x2 = []
midpoint_y2 = []


def circle(x, y):
    midpoint_x1.append(x)
    midpoint_y1.append(y)

    midpoint_x2.append(-x)
    midpoint_y2.append(-y)


radius = int(input('Enter radius value: '))

x = 0
y = radius
p = 1 - radius

while x <= y:
    circle(x, y)

    if p < 0:
        p = p + (2 * x) + 3
    else:
        p = p + (2 * (x - y)) + 5
        y -= 1
    x += 1

plt.figure("Midpoint Circle Drawing Algorithm")

plt.plot(midpoint_x1, midpoint_y1, color='red')
plt.plot(midpoint_y1, midpoint_x1, color='red')
plt.plot(midpoint_y2, midpoint_x1, color='red')
plt.plot(midpoint_x2, midpoint_y1, color='red')
plt.plot(midpoint_x2, midpoint_y2, color='red')
plt.plot(midpoint_y2, midpoint_x2, color='red')
plt.plot(midpoint_y1, midpoint_x2, color='red')
plt.plot(midpoint_x1, midpoint_y2, color='red')

plt.axis('square')
plt.show()
