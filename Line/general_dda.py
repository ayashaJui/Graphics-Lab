import matplotlib.pyplot as plt

print("Line Drawing Algorithm")
x1, y1 = input("Enter Starting Point(x1,y1) with comma: ").split(',')
x2, y2 = input("Enter Ending Point(x2,y2) with comma: ").split(',')

x1, x2, y1, y2 = float(x1), float(x2), float(y1), float(y2)

dx = x2 - x1
dy = y2 - y1

m = dy / dx
b = y1 - m * x1

gen_x = [x1]
gen_y = [y1]

dda_x = [x1]
dda_y = [y1]
d_x1 = x1
d_y1 = y1

if abs(m) <= 1:
    while x1 < x2:
        x1 += 1
        y1 = m * x1 + b
        d_y1 = d_y1 + m

        gen_x.append(x1)
        gen_y.append(y1)

        dda_x.append(x1)
        dda_y.append(round(d_y1))
else:
    while y1 < y2:
        y1 += 1
        x1 = (y1 - b) / m
        d_x1 = d_x1 + (1/m)

        gen_x.append(x1)
        gen_y.append(y1)

        dda_x.append(round(d_x1))
        dda_y.append(y1)

plt.figure("Line Drawing Algorithm")
plt.title("Line Draw")
plt.xlabel('X - Axis')
plt.ylabel('Y - Axis')

plt.plot(gen_x, gen_y, label="General Line Drawing", linestyle='-')
plt.plot(dda_x, dda_y, label="DDA Line Drawing", linestyle='--')
plt.legend()
plt.show()
