"""
Script Name: ListFileSize.py
Author: Zailani
Version: 1.0.0
Description: 
    This code is a Python script that lists all files in a directory and its 
    subdirectories, along with their sizes. It sorts the files in descending 
    order based on their sizes. The script takes the directory path as a 
    command line argument and prints the file paths and sizes to the console. 
    If no directory path is provided, it displays an error message.
"""

import os
import sys

def listFilesBySize(directory):
    # List to store file paths and sizes
    fileList = []

    # Traverse through the directory and its subdirectories
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Get the file path and size
            filePath = os.path.join(root, file)
            fileSize = os.path.getsize(filePath)
            # Append the file path and size to the list
            fileList.append((filePath, fileSize))

    # Sort the file list in descending order of size
    sortedFileList = sorted(fileList, key=lambda x: x[1], reverse=True)

    # Print the file paths and sizes
    for file in sortedFileList:
        print(file[0], " - Size:", file[1])


# Example usage
if len(sys.argv) == 2:
    directoryPath = sys.argv[1]
    listFilesBySize(directoryPath)
else:
    print("Please provide the directory path as a command line argument.")

