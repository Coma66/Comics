# Barcode Scanning
# Chris Galler
''' This file scans information from a barcode in an live camera feed '''

'''Need to install pyzbar and cv2 packages from Command Shell
pip install pyzbar
pip install opencv-python
Check the Visual Studio C++ Distibutable if there are issues inporting pyzbar '''

# Import the needed libraries
import cv2  # Read/Capture camera or images
from pyzbar.pyzbar import decode
import time

# Open and set size of camera
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # 3 - Width
cap.set(4, 480)  # 4 - Height

if not cap.isOpened():
    print('Cannot open camera')

while True:
    sucess, frame = cap.read()
    if not sucess:
        print('Cannot recieve frame, exiting...')
        break
    # Store and print the Data field
    for i in decode(frame):
        print(i.data.decode('utf-8'))
        time.sleep(5)
    
    cv2.imshow('Camera Window', frame)
    if cv2.waitKey(1) == ord('q'):
        break


cap.release
cv2.destroyAllWindows()