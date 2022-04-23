import matplotlib.pyplot as plt


def line(x1, y1, x2, y2):
    x = x1
    y = y1

    dx = x2 - x1
    dy = y2 - y1
    dT = 2 * (dy - dx)
    dS = 2 * dy
    d = (2 * dy) - dx

    X = [x]
    Y = [y]

    if x1 == x2:
        while y != y2:
            if y2 > y1:
                y += 1
            else:
                y -= 1
            X.append(x)
            Y.append(y)
    else:
        m = dy / dx
        if m < 1:
            while x < x2:
                x += 1
                if d < 0:
                    d += dS
                else:
                    y += 1
                    d += dT
                X.append(x)
                Y.append(y)

        else:
            while y < y2:
                y += 1
                if d < 0:
                    d = d + 2 * dx
                else:
                    x += 1
                    d = d + (2 * (dx - dy))
                X.append(x)
                Y.append(y)

    plt.plot(X, Y, color='black', linestyle='--')


x1, y1 = map(int, input("Enter First Co-ordinate with comma separated: ").split(","))
x2, y2 = map(int, input("Enter Second Co-ordinate with comma separated: ").split(","))

plt.figure("Rectangle Drawing")

line(x1, y1, x1, y2)
line(x1, y2, x2, y2)
line(x2, y2, x2, y1)
line(x1, y1, x2, y1)

plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')

plt.ylim(ymin=0)

plt.show()
