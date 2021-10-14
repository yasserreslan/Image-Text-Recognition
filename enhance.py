import cv2

def enhance(image):
    image = cv2.resize(image, (0,0), fx=12, fy=12, interpolation=cv2.INTER_CUBIC)
    thresh = cv2.threshold(image, 172, 255, cv2.THRESH_BINARY_INV)[1]
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2,2))
    close = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    result = cv2.cvtColor(close, cv2.COLOR_BGR2GRAY)
    

    return result