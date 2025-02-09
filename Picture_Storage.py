# Picture Storage Program
# Chris Galler
''' This file program takes pictures of cmoic books through a webcam and stores it in a folder corresponding to the CLZ index number. Requires a given .csv file with the index numbers for the comics'''

''' Need to install pyzbar and cv2 packages from Command Shell
pip install pyzbar
pip install opencv-python
Check the Visual Studio C++ Distibutable if there are issues inporting pyzbar '''

######################
# Import libraries
######################
import cv2  # Read/Capture camera or images
from pyzbar.pyzbar import decode
import time
import os
import csv

#####################
# Function definition
#####################
''' This function takes an index number and parent directory, creates the folder to store the pictures and changes the working directory to that new folder'''
def createFolder(index, parent):
    path = os.path.join(parent, index)
    os.mkdir(path)
    os.chdir(path)

'''  This function reads the csv file from CLZ and returns a list of the index numbers in a Python list '''
### NEED TO DO ###
def getIndexNums(csvFile):
    with open(csvFile, newline=''):
        indReader = csv.reader(csvFile)
        indexList = []
    return indexList

#####################
# Main Program
#####################

# Get parent directory from user
top = input('Please enter the directory in which to store the pictures: ')

# Get the list of indexs from the .csv file
# file = input('Please enter the csv file name: ')
# file = file + '.csv'
indexes = [12345, 67891]

# Open and set size of camera
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # 3 - Width
cap.set(4, 480)  # 4 - Height

if not cap.isOpened():
    print('Cannot open camera')

# Loop through the indexes of the comics
for i in indexes:
    createFolder(str(i), top)    # Make and change to the directory
    picCount = 1    # Set count for multiple pictures of the same comic
    while True:
        sucess, frame = cap.read()
        if not sucess:
            print('Cannot recieve frame, exiting...')
            break
        cv2.imshow('Camera Window', frame)  # Show the stream of video
        # Take the pictures and save it to a file in the folder
        if cv2.waitKey(1) == ord('p'):
            cv2.imwrite(str(i) + '_' + str(picCount) + '.jpg', frame)
            print(f'Successfully took picture {picCount}')
            picCount += 1
            time.sleep(1)

        if cv2.waitKey(1) == ord('q'):  # Stop taking pictures for this index
            print('Moving to next comic')
            time.sleep(3)
            break

cap.release
cv2.destroyAllWindows()