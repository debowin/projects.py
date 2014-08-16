"""
Python Script for making a list-file in the given directories. The list-file is a text file that contains the names
of the subdirectories and files contained within. Useful to keep track of the directory's contents eg. movies, songs,
episodes, software and games...

1) If list file already exists, overwrite it.
2) Don't consider any hidden or temporary files.
3) Differentiate between files and folders.
"""
import sys
import os

def main():
    if len(sys.argv) < 2:
        print "Usage: python ListFiles.py directory [, directories]"
    dirs = sys.argv[1:]  # get the list of directories to consider
    for dire in dirs:
        print "Creating list file for", dire,"..."
        dirList = [item for item in os.listdir(dire) if (item[0] != '.' and item[-1] != '~')]
        # ^ consider all files/folders except hidden and temporary ones
        if dire[-1] == '/':  # take care of the trailing /
            path = dire
        else:
            path = dire + "/"
        listFile = open(path + "list.txt", "w")  # create the list file in write mode in the considered directory
        listFile.write('Total: '+ str(len(dirList)) + ' items.\n')
        listFile.write('\n'.join([str(dirList.index(item) + 1) + ') ' + ('[dir]\t' if os.path.isdir(path + item) else '[file]\t') + item for item in dirList]))
        # ^ properly write out the list to the list file with numbering

if __name__ == "__main__":
    main()