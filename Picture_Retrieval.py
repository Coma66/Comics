# Picture Storage Program
# Chris Galler
''' This file program takes a list of indexes from a csv and retrieves the corresponding pictures (only the first one) from local storage.
It then stores those pictures into its own folder for easier retrieval. '''

''' Need to install pyzbar and cv2 packages from Command Shell
pip install pyzbar
pip install opencv-python
Check the Visual Studio C++ Distibutable if there are issues inporting pyzbar '''

######################
# Import libraries
######################
import tkinter.filedialog
import cv2  # Read/Capture camera or images
import os
import csv
import tkinter as tk

#####################
# Function definition
#####################
'''  This function reads the csv file from CLZ and returns a list of the index numbers, comic names, and issue numbers in respective Python lists '''
def getIndexNums(csvFile):
    indexList = []
    indInd = 0
    nameList = []
    indName = 0
    numList = []
    indNum = 0
    with open(csvFile, newline = '') as file:
        indReader = csv.reader(file)  # Create reader object
        headerLine = indReader.__next__()  # Store the first line of column headers
        for i in range(len(headerLine)):  # Iterate across the column headers
            if headerLine[i] == 'Index':  # Find the column of the Index numbers
                indInd = i
            elif headerLine[i] == 'Series':  # Find the column of the comic Name
                indName = i
            elif headerLine[i] == 'Issue Nr':  # Find the column of the comic issue numbers
                indNum = i
        for line in indReader:  # Store all the indexes and names into a list each to return
            if line[indInd] != '':
                indexList.append(line[indInd])
            if line[indName] != '':
                nameList.append(line[indName])
            if line[indNum] != '':
                numList.append(line[indNum])
    return indexList, nameList, numList

#####################
# Main Program
#####################

def main():
    # Get parent directory from user
    #top = input('Please enter the directory in which the pictures are stored with the csv file: ')
    top = tk.filedialog.askdirectory(title = 'Select a directory')

    # Change working directory to read csv file and retrieve pictures
    os.chdir(top)

    # Get the list of indexs from the .csv file
    file = tk.filedialog.askopenfilename(initialdir = top, title = 'Select a file', filetypes=(("CSV files","*.csv"), ("All files","*.*")))
    folder = file.replace('.csv', '') # Make new folder based on CSV file name
    indexes, names, issues = getIndexNums(file)

    #  Make a new folder to store all pictures
    newFold = os.path.join(top, folder)
    try:
        os.mkdir(newFold)
    except FileExistsError:
        print('Folder already exists, continuing on.')

    #  Initialize total picture counter, image list, new save name list, and which pic to grab from each index folder
    while True:
        try:
            picCount = int(input('Please enter the starting picture number for the sale folder: '))
        except ValueError:
            print("This isn't a valid number")
        else:
            break
    imageList = []
    imageName = []
    SOLD_PIC = 0

    #  Loop through the folders and copy the first picture in each folder to sold folder
    for i in range(0, len(indexes)):
        try:
            os.chdir(os.path.join(top, indexes[i]))  #  Change the directory to the current index picture folder
        except FileNotFoundError:
            print(f'File {indexes[i]} was not found, moving to next in the list.')
        pics = os.listdir()  #  Get the list of pictures in the folder

        #  Get first pic in folder
        imageList.append(cv2.imread(pics[SOLD_PIC]))  #  Read the first picture in the folder and add to the image list
        imageName.append(str(picCount) + '_' + pics[SOLD_PIC])  #  Add new save name to the image list
        picCount += 1  #  Increment the total picture counter

        #  Loop through the pictures in the folder (KEEPING FOR HISTORY, BUT ONLY NEED FIRST PICTURE FROM EACH INDEX FOLDER PER CUSTOMER REQUEST)
        # for j in range(0, len(pics)):
        #     imageList.append(cv2.imread(pics[j]))  #  Read the picture in the folder and add to the image list
        #     imageName.append(str(picCount) + '_' + pics[j])  #  Add new save name to the image list
        #     picCount += 1  #  Increment the total picture counter

    os.chdir(newFold)  #  Change directory to the new storage folder

    #  Loop through images and save to new folder
    for k in range(0, len(imageList)):
        try:
            cv2.imwrite(imageName[k], imageList[k])  #  Write the image to the new folder with a modified name
        except cv2.error:
            print(f'Image {imageName[k]} failed to write, moving to next image.')

main()