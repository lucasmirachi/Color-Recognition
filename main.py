import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
 
while True:
    success, img = cap.read()

    height, width, success = img.shape

    center_x = int(width/2)
    center_y = int(height/2)

    # setting the pixel we want to take the color value
    pixel_center = img[center_y, center_x]
    cv2.circle(img, (cx, cy), 5, (0, 255, 0), 3)

    #converting the image's BGR colorspace to HSV color space

    hsvImg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lowerLimit, upperLimit = get_limits(color=yellow)

    #creating a mask to gather all the pixels that belong to the color we want to detect
    mask = cv2.inRange(hsvImg, lowerLimit, upperLimit)

    #drawing a bounding box around the color object
    mask_ = Image.fromarray(mask)

    bbox = mask_.getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox

        img = cv2.rectangle(img, (x1, y1), (x2, y2), (0,255,0), 5)

    cv2.imshow('Image', mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()
