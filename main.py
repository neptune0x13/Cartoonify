import cv2
import easygui

from lib.cartoonify import Cartoonify


def main():
    cartoonifier = Cartoonify()
    image = easygui.fileopenbox()
    cartoonified = cartoonifier.cartoonify(image)
    cv2.imwrite("images/cartoonified.png", cartoonified)
    print("Cartoonified image stored at images/cartoonified.png")


if __name__ == "__main__":
    main()
