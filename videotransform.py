import numpy as np
import cv2
blurg3 = np.array((
	[1, 2, 1],
	[2, 4, 2],
	[1, 2, 1]), dtype="int")/16
blurg5 =  np.array((
	[1, 4, 6, 4, 1],
	[4, 16, 24, 16, 4],
        [6, 24, 36, 24, 6],
        [4, 16, 24, 16, 4],
	[1, 4, 6, 4, 1],), dtype="int")/256
laplacian = np.array((
	[0, 1, 0],
	[1, -4, 1],
	[0, 1, 0]), dtype="int")
# construct the Sobel x-axis kernel
sobelX = np.array((
	[-1, 0, 1],
	[-2, 0, 2],
	[-1, 0, 1]), dtype="int")
# construct the Sobel y-axis kernel
sobelY = np.array((
	[-1, -2, -1],
	[0, 0, 0],
	[1, 2, 1]), dtype="int")
edgek= np.array((
	[-1, -1, -1],
	[-1, 8, -1],
	[-1, -1, -1]), dtype="int")
cap = cv2.VideoCapture(0)

mode=''
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.filter2D(gray, -1, blurg3)
    sx = cv2.filter2D(gray, -1, sobelX)
    sy = cv2.filter2D(gray, -1, sobelY)
    lap = cv2.filter2D(gray, -1, laplacian)
    ed = cv2.filter2D(gray, -1, edgek)
    # Display the resulting frame
    if mode=='bluefire':
        disp=255-lap*5
        disp=cv2.cvtColor(disp, cv2.COLOR_GRAY2BGR)+frame
    if mode=='bismuth':
        disp = lap*5
        disp= frame * cv2.cvtColor(disp, cv2.COLOR_GRAY2BGR)
    #ret,disp = cv2.threshold(disp,47,255,cv2.THRESH_BINARY)
    cv2.imshow('frame',disp)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
