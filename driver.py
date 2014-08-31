__author__ = 'debowin'
import httplib2
import pprint
import mimetypes
import os
import sys
import difflib

from apiclient.discovery import build
from apiclient.http import MediaFileUpload
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.file import Storage

"""
This script lets users perform various operations on their Google drive accounts.
1. For upload, the file has to be in the same directory as the script.(MediaFileUpload issue)
2. Add a visual progress bar instead of percentages.(Done)
3. Perform fuzzy search.(Done using difflib)
4. Download links provided to user because downloading via HTTP request in the script itself is stupid for large files.

		*** Make sure you paste in your own client credentials in the script before running it *** 
"""


def print_list(results):
    """
    Prints out a neat list of files along with download/export links.
    :param results - list of files:
    :return:
    """
    for result in results:
        print '#\tTitle:',result['title']
        if 'webContentLink' in result.keys():
            # For binary files
            print '\tDownload Link:',result['webContentLink']
        else:
            # For Google Docs
            export_links = result['exportLinks']
            print '\tExport Links:'
            for mime_type in export_links.keys():
                print '\t\t'+mime_type, ':', export_links[mime_type]


def list_all(drive_service):
    """
    Gets a list of all the files on the user's Google Drive account.
    :param drive_service - Drive API service instance:
    :return results - list of user's Google Drive files:
    """
    results = []
    page_token = None
    while True:
        params = {}
        if page_token:
            params['page_token'] = page_token
        request = drive_service.files().list(**params)
        response = request.execute()
        results.extend(response['items'])
        page_token = response.get('nextPageToken')
        if not page_token:
            break
    # pprint.pprint(results)
    return results


def search_file(drive_service):
    """
    Perform a fuzzy search(>50%% match) on the user's Google Drive account.
    :param drive_service - Drive API service instance:
    :return match_results - list of matching files:
    """
    results = list_all(drive_service)
    results_by_title = [result['title'] for result in results]
    keyword = raw_input('Enter the search keyword: ')
    matches = difflib.get_close_matches(keyword,results_by_title,10,0.5) # Atmost 10 matches, 50% match accuracy
    print '%d match(es) found...' % len(matches)
    match_results = []
    for result in results:
        if result['title'] in matches:
            match_results.append(result)
    return match_results


def upload(drive_service):
    """
    Upload a file to the user's Google Drive.
    :param drive_service - Drive API service instance:
    :return:
    """
    # Get file path from the user
    file_path = raw_input('Please provide a path to the file: ')
    # Get file name from the path
    file_name = os.path.basename(file_path)
    # Guess mime type from extension
    mime_type = mimetypes.guess_type(file_name)[0]
    # Abort script if path is invalid
    if not os.path.exists(file_path):
        print file_name + " does not exist..."
        exit()
    else:
        print file_name + " found in given path..."
    # Allow user to specify a description or use default
    desc = raw_input("Please provide an additional description(or leave blank for default): ")
    if desc=='':
        desc = 'Uploaded using driver...'
    # Path to the file to upload
    FILENAME = file_path
    # Insert the file
    media_body = MediaFileUpload(FILENAME, mimetype=mime_type, resumable=True)
    body = {
      'title': file_name,
      'description': desc,
      'mimeType': mime_type
    }
    print 'Please wait while your file is being uploaded...'
    request = drive_service.files().insert(body=body, media_body=media_body)
    response = None
    while response is None:
      status, response = request.next_chunk()
      if status:
        bars = status.progress() * 20
        sys.stdout.write("\rProgress: [[%-20s]] %d%%" % ('='*int(bars),status.progress()*100))
        sys.stdout.flush()
    print "\rProgress: [%-20s] %d%%" % ('='*20,100)
    print "\nUpload Complete!\n"
    show_meta = raw_input('Would you like to see the metadata of the uploaded file?(y/n) ')
    if show_meta=='y':
        pprint.pprint(response)


def main():
    # Copy your credentials from the console http://console.developers.google.com
    CLIENT_ID = 'YOUR CLIENT ID'
    CLIENT_SECRET = 'YOUR CLIENT SECRET'

    # Check https://developers.google.com/drive/scopes for all available scopes
    OAUTH_SCOPE = 'https://www.googleapis.com/auth/drive'

    # Redirect URI for installed apps
    REDIRECT_URI = 'urn:ietf:wg:oauth:2.0:oob'

    # Run through the OAuth flow and retrieve credentials if not found in credential storage
    if(os.path.exists('user_credentials')):
        storage = Storage('user_credentials')
        credentials = storage.get()
    else:
        flow = OAuth2WebServerFlow(CLIENT_ID, CLIENT_SECRET, OAUTH_SCOPE, REDIRECT_URI)
        authorize_url = flow.step1_get_authorize_url()
        print 'Go to the following link in your browser: ' + authorize_url
        code = raw_input('Enter verification code: ').strip()
        credentials = flow.step2_exchange(code)
        storage = Storage('user_credentials')
        storage.put(credentials)

    # Create an httplib2.Http object and authorize it with our credentials
    http = httplib2.Http()
    http = credentials.authorize(http)

    drive_service = build('drive', 'v2', http=http)
    choice = int(raw_input('What would you like to do?\n1)Upload a file\n2)List all files\n3)Search for a file\nChoose: '))
    if choice==1:
        upload(drive_service)
    elif choice==2:
        results = list_all(drive_service)
        print_list(results)
    elif choice==3:
        match_results = search_file(drive_service)
        print_list(match_results)


if __name__=="__main__":
    main()
