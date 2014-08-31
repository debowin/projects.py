# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ListFiles.ui'
#
# Created: Fri Aug 29 01:40:15 2014
# by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

__author__ = 'debowin'
"""
Python Script for making a list-file in the given directories. The list-file is a text file that contains the names
of the subdirectories and files contained within. Useful to keep track of the directory's contents eg. movies, songs,
episodes, software and games...

1) If list file already exists, overwrite it.
2) Don't consider any hidden or temporary files or even existing list files.
3) Differentiate between files and folders.
"""
# Add icons for the buttons

from PyQt4 import QtCore, QtGui
import os, sys

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_Form(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)


    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(542, 525)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pbAddDir = QtGui.QPushButton(Form)
        self.pbAddDir.setStyleSheet(_fromUtf8("color: rgb(0, 170, 0);"))
        self.pbAddDir.setObjectName(_fromUtf8("pbAddDir"))
        self.horizontalLayout.addWidget(self.pbAddDir)
        self.pbRemDir = QtGui.QPushButton(Form)
        self.pbRemDir.setStyleSheet(_fromUtf8("color: rgb(255, 0, 0);"))
        self.pbRemDir.setObjectName(_fromUtf8("pbRemDir"))
        self.horizontalLayout.addWidget(self.pbRemDir)
        self.pbClearDirs = QtGui.QPushButton(Form)
        self.pbClearDirs.setObjectName(_fromUtf8("pbClearDirs"))
        self.horizontalLayout.addWidget(self.pbClearDirs)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.listDirs = QtGui.QListWidget(Form)
        self.listDirs.setObjectName(_fromUtf8("listDirs"))
        self.gridLayout.addWidget(self.listDirs, 2, 0, 1, 1)
        self.listFiles = QtGui.QListWidget(Form)
        self.listFiles.setObjectName(_fromUtf8("listFiles"))
        self.gridLayout.addWidget(self.listFiles, 2, 1, 1, 1)
        self.labelDirs = QtGui.QLabel(Form)
        self.labelDirs.setObjectName(_fromUtf8("labelDirs"))
        self.gridLayout.addWidget(self.labelDirs, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.labelFiles = QtGui.QLabel(Form)
        self.labelFiles.setObjectName(_fromUtf8("labelFiles"))
        self.gridLayout.addWidget(self.labelFiles, 1, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addLayout(self.gridLayout)
        self.pbGenList = QtGui.QPushButton(Form)
        self.pbGenList.setStyleSheet(_fromUtf8("color: rgb(0, 0, 255);"))
        self.pbGenList.setObjectName(_fromUtf8("pbGenList"))
        self.verticalLayout.addWidget(self.pbGenList)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "List Files", None))
        self.pbAddDir.setText(_translate("Form", "Add Directory (+)", None))
        self.pbRemDir.setText(_translate("Form", "Remove Directory (-)", None))
        self.pbClearDirs.setText(_translate("Form", "Clear All (X)", None))
        self.labelDirs.setText(_translate("Form", "Directories", None))
        self.labelFiles.setText(_translate("Form", "Directory Contents", None))
        self.pbGenList.setText(_translate("Form", "Generate List Files (=>)", None))

        self.pbAddDir.clicked.connect(self.addDir)
        self.pbRemDir.clicked.connect(self.remDir)
        self.pbClearDirs.clicked.connect(self.clearDirs)
        self.listDirs.clicked.connect(self.showFiles)
        self.listFiles.doubleClicked.connect(self.addDirFromList)
        self.pbGenList.clicked.connect(self.genListFiles)


    def addDir(self):
        """
        Opens a folder-only file dialog and adds the selected folder to the Directory List
        Checks if it already exists in the list.
        :return:
        """
        folder = QtGui.QFileDialog.getExistingDirectory(None, "Select a Directory")
        if folder == '':
            return
        # Remove possibility of adding duplicates.
        for item_index in range(self.listDirs.count()):
            if folder == self.listDirs.item(item_index).text():
                QtGui.QMessageBox.warning(self, "Wait a second!",
                                          "Looks like you already have this folder in the list.\n(%s)" % folder)
                return
        self.listDirs.addItem(folder)


    def addDirFromList(self):
        """
        Lets the user add a directory from the Content List of another Directory in the Directory List
        Checks if selected item is folder or not and also if it already exists in the list.
        :return:
        """
        selected_item = self.listFiles.currentItem().text()
        selected_dir = self.listDirs.currentItem().text()
        new_item = selected_dir + '/' + selected_item
        if not os.path.isdir(new_item):
            QtGui.QMessageBox.warning(self, "Wait a second!",
                                      "Looks like you are trying to add a file.\n(%s)\nThis only works with folders." % new_item)
            return
        for item_index in range(self.listDirs.count()):
            if new_item == self.listDirs.item(item_index).text():
                QtGui.QMessageBox.warning(self, "Wait a second!",
                                          "Looks like you already have this folder in the list.\n(%s)" % new_item)
                return
        self.listDirs.addItem(new_item)


    def remDir(self):
        """
        Removes the selected directory from the list.
        :return:
        """
        selected_item = self.listDirs.currentItem()
        if selected_item == None:
            QtGui.QMessageBox.warning(self, "Wait a second!", "Looks like you have nothing to remove.")
            return
        selected_row = self.listDirs.row(selected_item)
        # Confirmation Dialog
        sure = QtGui.QMessageBox.question(self, "Confirm", "Are you sure?",
                                          QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel, QtGui.QMessageBox.Cancel)
        if sure == QtGui.QMessageBox.Ok:
            self.listDirs.takeItem(selected_row)
            self.listFiles.clear()
        if self.listDirs.count() != 0:
            self.showFiles()


    def clearDirs(self):
        """
        Clears all the items in the Directory List.
        :return:
        """
        if self.listDirs.count() == 0:
            QtGui.QMessageBox.warning(self, "Wait a second!", "Looks like you have nothing to clear.")
            return
        # Confirmation Dialog
        sure = QtGui.QMessageBox.question(self, "Confirm", "Are you sure?",
                                          QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel, QtGui.QMessageBox.Cancel)
        if sure == QtGui.QMessageBox.Ok:
            self.listDirs.clear()
            self.listFiles.clear()


    def showFiles(self):
        """
        Shows the contents of the selected directory in the Directory List inside the Content List.
        :return:
        """
        self.listFiles.clear()
        path = self.listDirs.currentItem().text()
        dirList = [item for item in os.listdir(path) if (item[0] != '.' and item[-1] != '~' and item[0] != '$')]
        # ^ consider all files/folders except hidden and temporary ones.
        self.listFiles.addItems(dirList)


    def genListFiles(self):
        """
        Makes a list file in all of the directories in the Directory List.
        :return:
        """
        if self.listDirs.count() == 0:
            QtGui.QMessageBox.warning(self, "Wait a second!", "Looks like you forgot to add some directories.")
            return

        sure = QtGui.QMessageBox.question(self, "Confirm",
                                          "This will create/overwrite list files in all the selected directories. Are you sure?",
                                          QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel, QtGui.QMessageBox.Cancel)
        if sure == QtGui.QMessageBox.Cancel:
            return

        for item_index in range(self.listDirs.count()):
            path = self.listDirs.item(item_index).text() + '/'
            dirList = [item for item in os.listdir(path) if
                       (item[0] != '.' and item[-1] != '~' and item[0] != '$' and item != "list.txt")]
            listFile = open(path + "list.txt", "w")  # create the list file in write mode in the considered directory
            listFile.write('Total: ' + str(len(dirList)) + ' items.\n')
            listFile.write('\n'.join(
                [str(dirList.index(item) + 1) + ') ' + ('[dir]\t' if os.path.isdir(path + item) else '[file]\t') + item
                 for item in dirList]))
            # ^ properly write out the list to the list file with numbering
        QtGui.QMessageBox.information(self, "Success", "List files generated successfully!")


if __name__ == "__main__":
    sys.stderr = open(sys.argv[0][:-2]+"log", 'w') # Redirecting errors to logfile.
    app = QtGui.QApplication(sys.argv)
    ex = Ui_Form()
    ex.show()
    sys.exit(app.exec_())