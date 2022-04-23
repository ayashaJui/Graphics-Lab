import cv2
import numpy as np

x, y = None, None
drawing = False


def draw(event, curr_x, curr_y, flag, params):
    global x, y, drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True  # enable drawing
        x, y = curr_x, curr_y   # update co-ordinates

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.line(canvas, (curr_x, curr_y), (x, y), (0, 0, 0), thickness=3)
            x, y = curr_x, curr_y  # update co-ordinates

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False     # disable drawing


def dda_line(*args):
    print("DDA Line Drawing Algorithm")


def bres_line(*args):
    print("Bresenham's Line Drawing Algorithm")


canvas = np.zeros((500, 500, 3), dtype=np.uint8)
canvas.fill(255)

cv2.namedWindow('Draw')

cv2.setMouseCallback('Draw', draw)

cv2.createButton('DDA Line', dda_line)
cv2.createButton('Bresenham\'s Line', bres_line)

while True:
    cv2.imshow('Draw', canvas)  # update canvas

    # break out of loop on 'Esc'
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
