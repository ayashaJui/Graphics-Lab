import matplotlib.pyplot as plt

x1 = []
y1 = []
x2 = []
y2 = []


def ellipse(x, y):
    x1.append(x)
    y1.append(y)

    x2.append(-x)
    y2.append(-y)


def midpoint_ellipse(a, b):
    x = 0
    y = b
    aa = a * a
    bb = b * b
    aa2 = aa * 2
    bb2 = bb * 2
    fx = bb2 * x
    fy = aa2 * y
    p = bb - aa * b + 0.25 * aa

    while fx < fy:
        ellipse(x, y)
        x += 1
        fx = fx + bb2

        if p < 0:
            p = p + fx + bb
        else:
            y -= 1
            fy = fy - aa2
            p = p + fx + bb - fy

    ellipse(x, y)

    p = bb * (x + 0.5) * (x + 0.5) + aa * (y - 1) * (y - 1) - aa * bb

    while y > 0:
        y -= 1
        fy = fy - aa2

        if p >= 0:
            p = p - fy + aa
        else:
            x += 1
            fx = fx + bb2
            p = p + fx - fy + aa

        ellipse(x, y)


a, b = map(int, input("Enter length of Major and Minor axis with comma separated: ").split(","))

midpoint_ellipse(a, b)

plt.figure("Midpoint Ellipse Algorithm")
plt.plot(x1, y1, color='black')
plt.plot(x2, y2, color='black')
plt.plot(x1, y2, color='black')
plt.plot(x2, y1, color='black')

plt.axis('Square')
plt.show()
