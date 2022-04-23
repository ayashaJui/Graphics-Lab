import matplotlib.pyplot as plt

print("Line Drawing Algorithm")
x1, y1 = input("Enter Initial Point(x1,y1) with comma: ").split(',')
x2, y2 = input("Enter End Point(x2,y2) with comma: ").split(',')

x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)

dx = x2 - x1
dy = y2 - y1

m = dy / dx
b = y1 - m * x1

gen_x = [x1]
gen_y = [y1]

if m <= 1:
    while x1 < x2:
        x1 += 1
        y1 = m * x1 + b

        gen_x.append(x1)
        gen_y.append(y1)
else:
    while y1 < y2:
        y1 += 1
        x1 = (y1 - b) / m

        gen_x.append(x1)
        gen_y.append(y1)

print(gen_x, gen_y)
plt.figure("Line Drawing Algorithm")
plt.title("Line Draw")
plt.xlabel('X - Axis')
plt.ylabel('Y - Axis')

plt.plot(gen_x, gen_y, label="General Line Drawing")
plt.legend()
plt.show()
