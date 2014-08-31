# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Driver.ui'
#
# Created: Sat Aug 30 15:54:07 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

__author__ = 'debowin'

from PyQt4 import QtCore, QtGui
import httplib2
import mimetypes
import webbrowser
import os
import sys
import pprint

from apiclient.discovery import build
from apiclient.http import MediaFileUpload
from oauth2client.client import FlowExchangeError
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.file import Storage

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
        self.credentials = None
        self.drive_service = None

        #Copy your credentials from the console http://console.developers.google.com
        CLIENT_ID = 'YOUR CLIENT ID'
        CLIENT_SECRET = 'YOUR CLIENT SECRET'

        # Check https://developers.google.com/drive/scopes for all available scopes
        OAUTH_SCOPE = 'https://www.googleapis.com/auth/drive'

        # Redirect URI for installed apps
        REDIRECT_URI = 'urn:ietf:wg:oauth:2.0:oob'
        self.flow = OAuth2WebServerFlow(CLIENT_ID, CLIENT_SECRET, OAUTH_SCOPE, REDIRECT_URI)
        self.setupUi(self)
        self.tabWidget.setCurrentIndex(0)
        self.generateAuthData()
        if self.credentials != None:
            self.createService()
        self.fetchList()

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(445, 547)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gbAuth = QtGui.QGroupBox(Form)
        self.gbAuth.setEnabled(True)
        self.gbAuth.setObjectName(_fromUtf8("gbAuth"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.gbAuth)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label = QtGui.QLabel(self.gbAuth)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_3.addWidget(self.label)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.leAuth = QtGui.QLineEdit(self.gbAuth)
        self.leAuth.setObjectName(_fromUtf8("leAuth"))
        self.horizontalLayout_3.addWidget(self.leAuth)
        self.pbOpenLink = QtGui.QPushButton(self.gbAuth)
        self.pbOpenLink.setObjectName(_fromUtf8("pbOpenLink"))
        self.horizontalLayout_3.addWidget(self.pbOpenLink)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.leVerify = QtGui.QLineEdit(self.gbAuth)
        self.leVerify.setObjectName(_fromUtf8("leVerify"))
        self.verticalLayout_3.addWidget(self.leVerify)
        self.pbAuth = QtGui.QPushButton(self.gbAuth)
        self.pbAuth.setObjectName(_fromUtf8("pbAuth"))
        self.verticalLayout_3.addWidget(self.pbAuth)
        self.verticalLayout_2.addWidget(self.gbAuth)
        self.tabWidget = QtGui.QTabWidget(Form)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.upload = QtGui.QWidget()
        self.upload.setObjectName(_fromUtf8("upload"))
        self.verticalLayout = QtGui.QVBoxLayout(self.upload)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(self.upload)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_5.addWidget(self.label_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.leUpload = QtGui.QLineEdit(self.groupBox)
        self.leUpload.setObjectName(_fromUtf8("leUpload"))
        self.horizontalLayout_2.addWidget(self.leUpload)
        self.pbBrowse = QtGui.QPushButton(self.groupBox)
        self.pbBrowse.setObjectName(_fromUtf8("pbBrowse"))
        self.horizontalLayout_2.addWidget(self.pbBrowse)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_5.addWidget(self.label_2)
        self.pteDesc = QtGui.QPlainTextEdit(self.groupBox)
        self.pteDesc.setFrameShadow(QtGui.QFrame.Sunken)
        self.pteDesc.setTabChangesFocus(True)
        self.pteDesc.setOverwriteMode(False)
        self.pteDesc.setBackgroundVisible(False)
        self.pteDesc.setObjectName(_fromUtf8("pteDesc"))
        self.verticalLayout_5.addWidget(self.pteDesc)
        self.pbUpload = QtGui.QPushButton(self.groupBox)
        self.pbUpload.setObjectName(_fromUtf8("pbUpload"))
        self.verticalLayout_5.addWidget(self.pbUpload)
        self.progressBar = QtGui.QProgressBar(self.groupBox)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout_5.addWidget(self.progressBar)
        self.verticalLayout.addWidget(self.groupBox)
        self.tabWidget.addTab(self.upload, _fromUtf8(""))
        self.listAll = QtGui.QWidget()
        self.listAll.setObjectName(_fromUtf8("listAll"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.listAll)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.treeFiles = QtGui.QTreeWidget(self.listAll)
        self.treeFiles.setObjectName(_fromUtf8("treeFiles"))
        self.verticalLayout_4.addWidget(self.treeFiles)
        self.tabWidget.addTab(self.listAll, _fromUtf8(""))
        self.searchFile = QtGui.QWidget()
        self.searchFile.setObjectName(_fromUtf8("searchFile"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.searchFile)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.leSearch = QtGui.QLineEdit(self.searchFile)
        self.leSearch.setObjectName(_fromUtf8("leSearch"))
        self.horizontalLayout.addWidget(self.leSearch)
        self.pbSearch = QtGui.QPushButton(self.searchFile)
        self.pbSearch.setObjectName(_fromUtf8("pbSearch"))
        self.horizontalLayout.addWidget(self.pbSearch)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.treeResults = QtGui.QTreeWidget(self.searchFile)
        self.treeResults.setObjectName(_fromUtf8("treeResults"))
        self.verticalLayout_6.addWidget(self.treeResults)
        self.tabWidget.addTab(self.searchFile, _fromUtf8(""))
        self.verticalLayout_2.addWidget(self.tabWidget)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Driver", None))
        self.gbAuth.setTitle(_translate("Form", "Authentication", None))
        self.label.setText(_translate("Form", "Provide access to your Google Drive Account:", None))
        self.leAuth.setPlaceholderText(_translate("Form", "OAuth2 Link", None))
        self.pbOpenLink.setText(_translate("Form", "Open Link in Browser", None))
        self.leVerify.setPlaceholderText(_translate("Form", "Enter the Verification Code here", None))
        self.pbAuth.setText(_translate("Form", "Authenticate Application", None))
        self.label_3.setText(_translate("Form", "Select a file to upload to your Drive:", None))
        self.pbBrowse.setText(_translate("Form", "Browse", None))
        self.label_2.setText(_translate("Form", "Enter a description: (Leave blank for default)", None))
        self.pbUpload.setText(_translate("Form", "Upload", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.upload), _translate("Form", "Upload", None))
        self.treeFiles.headerItem().setText(0, _translate("Form", "Files in User\'s Drive", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.listAll), _translate("Form", "List All", None))
        self.leSearch.setPlaceholderText(_translate("Form", "Search Query", None))
        self.pbSearch.setText(_translate("Form", "Search", None))
        self.treeResults.headerItem().setText(0, _translate("Form", "Matching Files", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.searchFile), _translate("Form", "Search File", None))

        self.pbAuth.clicked.connect(self.authorize)
        self.pbOpenLink.clicked.connect(self.openLink)

    def createService(self):
        http = httplib2.Http()
        http = self.credentials.authorize(http)
        self.drive_service = build('drive', 'v2', http=http)
    def generateAuthData(self):
        # Run through the OAuth flow and retrieve credentials if not found in credential storage
        if(os.path.exists('user_credentials')):
            storage = Storage('user_credentials')
            self.credentials = storage.get()
            self.gbAuth.hide()
        else:
            authorize_url = self.flow.step1_get_authorize_url()
            self.leAuth.setText(authorize_url)
            self.leAuth.setReadOnly(True)

    def authorize(self):
        code = str(self.leVerify.text())
        if(code==''):
            QtGui.QMessageBox.warning(self, "Wait a second!",
                                      "Looks like you didn't enter a Verification Code.")
            return
        try:
            self.credentials = self.flow.step2_exchange(code)
        except FlowExchangeError:
            QtGui.QMessageBox.warning(self, "Wait a second!",
                                      "Looks like your Verification Code isn't valid.")
            return
        storage = Storage('user_credentials')
        storage.put(self.credentials)
        QtGui.QMessageBox.information(self, "Success",
                                      "Driver has been successfully authorized.")
        self.gbAuth.hide()
        self.createService()

    def openLink(self):
        link = str(self.leAuth.text())
        webbrowser.open(link,0,True)

    def fetchList(self, folder_id = 'root', tree_parent = None):
        page_token = None
        while True:
            params = {}
            if page_token:
                params['page_token'] = page_token
            params['q'] = 'trashed=false' # Query String
            request = self.drive_service.children().list(folderId = folder_id, **params)
            response = request.execute()
            for child in response['items']:
                tree_item = QtGui.QTreeWidgetItem()
                meta = self.getFileInfo(child['id'])
                tree_item.setText(0,meta['title'])
                # pprint.pprint(meta)
                if 'exportLinks' in meta.keys():
                    # Google Format
                    pass
                elif 'webContentLink' in meta.keys():
                    # Binary File
                    pass
                else:
                    # Folder
                    self.fetchList(child['id'], tree_item)
                if(tree_parent == None):
                    self.treeFiles.addTopLevelItem(tree_item)
                else:
                    tree_parent.addChild(tree_item)
            page_token = response.get('nextPageToken')
            if not page_token:
                break

    def getFileInfo(self, file_id):
        return self.drive_service.files().get(fileId=file_id).execute()

    def searchFile(self):
        query = self.leSearch
        self.drive_service.files()
        # Only show files with shared==false

if __name__ == "__main__":
    # sys.stderr = open(sys.argv[0][:-2]+"log", 'w') # Redirecting errors to logfile.
    app = QtGui.QApplication(sys.argv)
    ex = Ui_Form()
    ex.show()
    sys.exit(app.exec_())

