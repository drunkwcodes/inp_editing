import csv

import cv2

# import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image


def main():
    # Read image and show
    imagePath = "pnlgds.png"
    image = cv2.imread(imagePath)
    plt.imshow(image)
    plt.axis("off")  # 隱藏座標軸
    plt.show()

    # Convert to black white
    image = Image.open(imagePath)
    threshold = 220
    bw_image = image.convert("L").point(lambda p: 255 if p > threshold else 0, "1")
    bw_path = "bw.png"
    bw_image.save(bw_path)

    # Gray scale
    imageGray = cv2.imread(bw_path, cv2.IMREAD_GRAYSCALE)

    # Resize
    imageResize200x200 = cv2.resize(imageGray, (200, 200))
    imageResize100x100 = cv2.resize(imageGray, (100, 100))
    imageResize20x20 = cv2.resize(imageGray, (20, 20))

    cv2.imwrite("resized_200x200.bmp", imageResize200x200)
    cv2.imwrite("resized_100x100.bmp", imageResize100x100)
    cv2.imwrite("resized_20x20.bmp", imageResize20x20)


if __name__ == "__main__":
    main()
