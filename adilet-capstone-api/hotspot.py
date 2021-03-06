import cv2
import flirimageextractor
import numpy as np


def hotspotFinder(img_path):
    ir_image = flirimageextractor.FlirImageExtractor()
    ir_image.process_image(img_path)
    temps = ir_image.get_thermal_np()
    max_temp = np.max(temps)
    # 4 is the ratio between temperature array and image
    coord = np.where(temps == max_temp) * np.array(4)
    return coord, max_temp

def find_hotspot(img_path):
    # find points
    hotspot = hotspotFinder(img_path)
    # Take reversively
    x = hotspot[0][1]
    y = hotspot[0][0]
    z = round(hotspot[1], 2)
    # biasing points
    w = 220
    h = 50

    # generate image
    img = cv2.imread(img_path)
    cv2.circle(img, (x, y), 3, (0, 0, 0), -1)
    cv2.line(img, (x, y), (w, h), 1)
    cv2.circle(img, (w, h), 3, (0, 0, 0), -1)
    cv2.putText(img, "Hotspot " + str(z) + ' C', (w - 50, h - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
    return img
