import cv2


def cartoonify(imagePath):
    """
    Cartoonify Image
    :param imagePath: path to original image
    :return: Cartoonified Image
    """
    orgImg = cv2.imread(imagePath)
    # orgImg = cv2.cvtColor(orgImg, cv2.COLOR_RGB2RGB)
    grayImg = cv2.cvtColor(orgImg, cv2.COLOR_BGR2GRAY)
    smooth = cv2.medianBlur(grayImg, 5)
    getEdge = cv2.adaptiveThreshold(smooth, 255,
                                    cv2.ADAPTIVE_THRESH_MEAN_C,
                                    cv2.THRESH_BINARY, 9, 9)
    colorImg = cv2.bilateralFilter(orgImg, 9, 300, 300)
    cartoon = cv2.bitwise_and(colorImg, colorImg, mask=getEdge)
    return cartoon
