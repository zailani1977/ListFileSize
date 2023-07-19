# ListFileSize
This is a Python script that lists all files in a directory and its subdirectories, along with their sizes. It sorts the files in descending order based on their sizes. The script takes the directory path as a command line argument and prints the file paths and sizes to the console. If no directory path is provided, it displays an error message.

# Usage
python ListFileSize.py <directory_path>

Replace <directory_path> with the actual directory path you want to list the files and sizes for.

# Requirements
This script requires Python 3.x or higher. No additional packages or libraries are needed.

# Example
$ python ListFileSize.py /path/to/directory


Output:

/path/to/directory/file3.txt - Size: 1000

/path/to/directory/subdirectory/file6.txt - Size: 500

/path/to/directory/file1.txt - Size: 300

/path/to/directory/subdirectory/file5.txt - Size: 200

/path/to/directory/subdirectory/file4.txt - Size: 150

/path/to/directory/file2.txt - Size: 100

List files in a specified directory and its subdirectories and sort them according to their size in descending order
