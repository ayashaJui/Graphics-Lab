import matplotlib.pyplot as plt
from numpy import Infinity
import math


def dda_line(i, x1, y1, x2, y2):
    x1, y1, x2, y2 = round(x1), round(y1), round(x2), round(y2)
    dx = x2 - x1
    dy = y2 - y1

    if dx != 0:
        m = abs(dy)/abs(dx)
    else:
        m = Infinity

    x = x1
    y = y1

    x_coordinate[i].append(round(x))
    y_coordinate[i].append(round(y))
    if m < 1:
        while x != x2:
            x_coordinate[i].append(round(x))
            y_coordinate[i].append(round(y))
            if x < x2:
                x += 1
            else:
                x -= 1
            if y2 > y1:
                y = y + m
            else:
                y = y - m

    else:
        while y != y2:
            x_coordinate[i].append(round(x))
            y_coordinate[i].append(round(y))
            if y < y2:
                y += 1
            else:
                y -= 1
            if m == Infinity:
                continue
            elif x2 > x1:
                x = x + (1/m)
            else:
                x = x - (1/m)


def rotate(rect_x, rect_y, center_x, center_y, angle, axis):
    if axis == 'x':
        return round((rect_x - center_x) * math.cos(math.radians(angle)) -
                     (rect_y - center_y) * math.sin(math.radians(angle)) + center_x)
    elif axis == 'y':
        return round((rect_y - center_y) * math.cos(math.radians(angle)) +
                     (rect_x - center_x) * math.sin(math.radians(angle)) + center_y)


# Defining rectangle 1
rect1_x1, rect1_y1, rect1_x3, rect1_y3 = 10, 20, 100, 520

# Rotating angle for 3 rectangles
rect1_angle = float(input("Enter First angle: "))
rect2_angle = float(input("Enter Second angle: "))
rect3_angle = float(input("Enter Third angle: "))

x_coordinate = [[], [], [], [], [], []]
y_coordinate = [[], [], [], [], [], []]

# Rotating rectangle 1
rect1_center_x, rect1_center_y = (rect1_x1 + rect1_x3) / 2, (rect1_y1 + rect1_y3) / 2

rect1_new_x1 = rotate(rect1_x1, rect1_y1, rect1_center_x, rect1_center_y, rect1_angle, 'x')
rect1_new_y1 = rotate(rect1_x1, rect1_y1, rect1_center_x, rect1_center_y, rect1_angle, 'y')
rect1_new_x2 = rotate(rect1_x3, rect1_y1, rect1_center_x, rect1_center_y, rect1_angle, 'x')
rect1_new_y2 = rotate(rect1_x3, rect1_y1, rect1_center_x, rect1_center_y, rect1_angle, 'y')
rect1_new_x3 = rotate(rect1_x3, rect1_y3, rect1_center_x, rect1_center_y, rect1_angle, 'x')
rect1_new_y3 = rotate(rect1_x3, rect1_y3, rect1_center_x, rect1_center_y, rect1_angle, 'y')
rect1_new_x4 = rotate(rect1_x1, rect1_y3, rect1_center_x, rect1_center_y, rect1_angle, 'x')
rect1_new_y4 = rotate(rect1_x1, rect1_y3, rect1_center_x, rect1_center_y, rect1_angle, 'y')


# Rotating rectangle 2
rect2_x1, rect2_y1, rect2_x3, rect2_y3 = \
    rect1_x1, rect1_y3, (rect1_x1 - (rect1_x3 - rect1_x1)), (rect1_y3 - (rect1_y3 - rect1_y1)/4)
rect2_center_x, rect2_center_y = (rect2_x1 + rect2_x3) / 2, (rect2_y1 + rect2_y3) / 2

rect2_angle += rect1_angle

rect2_new_x1 = rotate(rect2_x1, rect2_y1, rect2_center_x, rect2_center_y, rect2_angle, 'x')
rect2_new_y1 = rotate(rect2_x1, rect2_y1, rect2_center_x, rect2_center_y, rect2_angle, 'y')
rect2_new_x2 = rotate(rect2_x3, rect2_y1, rect2_center_x, rect2_center_y, rect2_angle, 'x')
rect2_new_y2 = rotate(rect2_x3, rect2_y1, rect2_center_x, rect2_center_y, rect2_angle, 'y')
rect2_new_x3 = rotate(rect2_x3, rect2_y3, rect2_center_x, rect2_center_y, rect2_angle, 'x')
rect2_new_y3 = rotate(rect2_x3, rect2_y3, rect2_center_x, rect2_center_y, rect2_angle, 'y')
rect2_new_x4 = rotate(rect2_x1, rect2_y3, rect2_center_x, rect2_center_y, rect2_angle, 'x')
rect2_new_y4 = rotate(rect2_x1, rect2_y3, rect2_center_x, rect2_center_y, rect2_angle, 'y')

rect12_x_diff, rect12_y_diff = rect1_new_x4 - rect2_new_x1, rect1_new_y4 - rect2_new_y1

rect2_new_x1, rect2_new_y1 = rect2_new_x1 + rect12_x_diff, rect2_new_y1 + rect12_y_diff
rect2_new_x2, rect2_new_y2 = rect2_new_x2 + rect12_x_diff, rect2_new_y2 + rect12_y_diff
rect2_new_x3, rect2_new_y3 = rect2_new_x3 + rect12_x_diff, rect2_new_y3 + rect12_y_diff
rect2_new_x4, rect2_new_y4 = rect2_new_x4 + rect12_x_diff, rect2_new_y4 + rect12_y_diff


# Rotating rectangle 3
rect3_x1, rect3_y1, rect3_x3, rect3_y3 = \
    rect2_x3, rect2_y3, (rect2_x3 + (rect2_x1 - rect2_x3)/4), (rect2_y3 - (rect2_y1 - rect2_y3))
rect3_center_x, rect3_center_y = (rect3_x1 + rect3_x3) / 2, (rect3_y1 + rect3_y3) / 2

rect3_angle += rect2_angle

rect3_new_x1 = rotate(rect3_x1, rect3_y1, rect3_center_x, rect3_center_y, rect3_angle, 'x')
rect3_new_y1 = rotate(rect3_x1, rect3_y1, rect3_center_x, rect3_center_y, rect3_angle, 'y')
rect3_new_x2 = rotate(rect3_x3, rect3_y1, rect3_center_x, rect3_center_y, rect3_angle, 'x')
rect3_new_y2 = rotate(rect3_x3, rect3_y1, rect3_center_x, rect3_center_y, rect3_angle, 'y')
rect3_new_x3 = rotate(rect3_x3, rect3_y3, rect3_center_x, rect3_center_y, rect3_angle, 'x')
rect3_new_y3 = rotate(rect3_x3, rect3_y3, rect3_center_x, rect3_center_y, rect3_angle, 'y')
rect3_new_x4 = rotate(rect3_x1, rect3_y3, rect3_center_x, rect3_center_y, rect3_angle, 'x')
rect3_new_y4 = rotate(rect3_x1, rect3_y3, rect3_center_x, rect3_center_y, rect3_angle, 'y')

rect23_x_diff, rect23_y_diff = rect2_new_x3 - rect3_new_x1, rect2_new_y3 - rect3_new_y1

rect3_new_x1, rect3_new_y1 = rect3_new_x1 + rect23_x_diff, rect3_new_y1 + rect23_y_diff
rect3_new_x2, rect3_new_y2 = rect3_new_x2 + rect23_x_diff, rect3_new_y2 + rect23_y_diff
rect3_new_x3, rect3_new_y3 = rect3_new_x3 + rect23_x_diff, rect3_new_y3 + rect23_y_diff
rect3_new_x4, rect3_new_y4 = rect3_new_x4 + rect23_x_diff, rect3_new_y4 + rect23_y_diff


# Drawing first rectangle
i = 0

dda_line(i, rect1_x1, rect1_y1, rect1_x3, rect1_y1)
dda_line(i, rect1_x3, rect1_y1, rect1_x3, rect1_y3)
dda_line(i, rect1_x3, rect1_y3, rect1_x1, rect1_y3)
dda_line(i, rect1_x1, rect1_y3, rect1_x1, rect1_y1)

# Drawing second rectangle
i += 1

dda_line(i, rect2_x1, rect2_y1, rect2_x3, rect2_y1)
dda_line(i, rect2_x3, rect2_y1, rect2_x3, rect2_y3)
dda_line(i, rect2_x3, rect2_y3, rect2_x1, rect2_y3)
dda_line(i, rect2_x1, rect2_y3, rect2_x1, rect2_y1)

# Drawing third rectangle
i += 1

dda_line(i, rect3_x1, rect3_y1, rect3_x3, rect3_y1)
dda_line(i, rect3_x3, rect3_y1, rect3_x3, rect3_y3)
dda_line(i, rect3_x3, rect3_y3, rect3_x1, rect3_y3)
dda_line(i, rect3_x1, rect3_y3, rect3_x1, rect3_y1)


# Drawing rotated rectangle 1
i += 1

dda_line(i, rect1_new_x1, rect1_new_y1, rect1_new_x2, rect1_new_y2)
dda_line(i, rect1_new_x2, rect1_new_y2, rect1_new_x3, rect1_new_y3)
dda_line(i, rect1_new_x3, rect1_new_y3, rect1_new_x4, rect1_new_y4)
dda_line(i, rect1_new_x4, rect1_new_y4, rect1_new_x1, rect1_new_y1)

# Drawing rotated rectangle 2
i += 1

dda_line(i, rect2_new_x1, rect2_new_y1, rect2_new_x2, rect2_new_y2)
dda_line(i, rect2_new_x2, rect2_new_y2, rect2_new_x3, rect2_new_y3)
dda_line(i, rect2_new_x3, rect2_new_y3, rect2_new_x4, rect2_new_y4)
dda_line(i, rect2_new_x4, rect2_new_y4, rect2_new_x1, rect2_new_y1)

# Drawing rotated rectangle 3
i += 1

dda_line(i, rect3_new_x1, rect3_new_y1, rect3_new_x2, rect3_new_y2)
dda_line(i, rect3_new_x2, rect3_new_y2, rect3_new_x3, rect3_new_y3)
dda_line(i, rect3_new_x3, rect3_new_y3, rect3_new_x4, rect3_new_y4)
dda_line(i, rect3_new_x4, rect3_new_y4, rect3_new_x1, rect3_new_y1)

# Plot the rectangles
plt.figure('Initial')
plt.plot(x_coordinate[0], y_coordinate[0], color="black")
plt.plot(x_coordinate[1], y_coordinate[1], color="black")
plt.plot(x_coordinate[2], y_coordinate[2], color="black")
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.axis('Square')

plt.figure('Rotated')
plt.plot(x_coordinate[3], y_coordinate[3], color="black")
plt.plot(x_coordinate[4], y_coordinate[4], color="black")
plt.plot(x_coordinate[5], y_coordinate[5], color="black")
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.axis('Square')

plt.show()
