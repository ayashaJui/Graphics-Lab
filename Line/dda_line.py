import matplotlib.pyplot as plt

print("Line Drawing Algorithm")
x1, y1 = input("Enter Initial Point(x1,y1) with comma: ").split(',')
x2, y2 = input("Enter End Point(x2,y2) with comma: ").split(',')

x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)

dx = x2 - x1
dy = y2 - y1

m = dy / dx

dda_x = [x1]
dda_y = [y1]

if abs(m) <= 1:
    while x1 < x2:
        x1 += 1
        y1 = y1 + m

        dda_x.append(x1)
        dda_y.append(round(y1))
else:
    while y1 < y2:

        y1 += 1
        x1 = x1 + (1/m)

        dda_x.append(round(x1))
        dda_y.append(y1)

print(dda_x, dda_y)
plt.figure("Line Drawing Algorithm")
plt.title("Line Draw")
plt.xlabel('X - Axis')
plt.ylabel('Y - Axis')

plt.plot(dda_x, dda_y, label="DDA Line Drawing")
plt.legend()
plt.show()
