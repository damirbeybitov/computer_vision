import cv2
import numpy as np

# events = [i for i in dir(cv) if 'EVENT' in i]
# print( events )

def update_brush_radius(value):
    global brush_radius
    brush_radius = value

def update_brush_color(channel, value):
    global brush_color
    brush_color[channel] = value

def draw_circle(event, x, y, flags, param):
    global drawing, s
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        cv2.circle(img, (x, y), brush_radius, tuple(brush_color), -1)
    elif event == cv2.EVENT_MOUSEMOVE and drawing:
        cv2.circle(img, (x, y), brush_radius, tuple(brush_color), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False



img = 255*np.ones((512, 1024, 3), np.uint8)
cv2.namedWindow('Paint Application')

brush_color = [0, 0, 0]
brush_radius = 10

cv2.createTrackbar('Radius', 'Paint Application', brush_radius, 50, update_brush_radius)
cv2.createTrackbar('Blue', 'Paint Application', 0, 255, lambda x: update_brush_color(0, x))
cv2.createTrackbar('Green', 'Paint Application', 0, 255, lambda x: update_brush_color(1, x))
cv2.createTrackbar('Red', 'Paint Application', 0, 255, lambda x: update_brush_color(2, x))

drawing = False
cv2.setMouseCallback('Paint Application', draw_circle)

while True:
    cv2.imshow('Paint Application', img)
    # ESC key = 27
    if cv2.waitKey(1) == 27:
        break
    if cv2.getWindowProperty('Paint Application', cv2.WND_PROP_VISIBLE) < 1:
        break

cv2.destroyAllWindows()


















