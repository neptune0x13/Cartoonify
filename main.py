# TODO: Streamlit app
import cv2

from cartoonify import cartoonify

image = input("Image File name: ")
cartoonified = cartoonify(image)
cv2.imshow('cartoon', cartoonified)
cv2.waitKey(3000)
cv2.imwrite("cartoonified.png", cartoonified)
cv2.destroyAllWindows()
