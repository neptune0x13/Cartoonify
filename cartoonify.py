import cv2
from numpy import ndarray


def cartoonify(imagePath: str) -> ndarray:
    """
    Cartoonify Image
    :param imagePath: path to original image
    :return: Cartoonified Image
    """
    # Reading the Image
    img = cv2.imread(imagePath)

    # Converting to Grayscale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Applying blur to image
    img_blur = cv2.medianBlur(img_gray, 5)

    # Getting the edges
    img_edges = cv2.adaptiveThreshold(img_blur, 255,
                                      cv2.ADAPTIVE_THRESH_MEAN_C,
                                      cv2.THRESH_BINARY, 9, 9)

    # Smoothening and Reducing noise w/o loss in edges
    img_smooth = cv2.bilateralFilter(img, 9, 300, 300)

    # Combining smoothened image and edges
    img_cartoon = cv2.bitwise_and(img_smooth, img_smooth, mask=img_edges)
    return img_cartoon
