from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
import io
import os

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive']
TOKEN_PATH = os.path.join(os.path.dirname(__file__), 'token.pickle')


class Image_to_Text:
    def __init__(self):
        self.service = None
        self.connect_google_drive()

    def connect_google_drive(self):
        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists(TOKEN_PATH):
            print("Loading token")
            with open(TOKEN_PATH, 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server()
            # Save the credentials for the next run
            with open(TOKEN_PATH, 'wb') as token:
                pickle.dump(creds, token)

        self.service = build('drive', 'v3', credentials=creds)

    def image2text(self, imgfile):
        result = io.BytesIO()

        mime = 'application/vnd.google-apps.document'
        res = self.service.files().create(
            body={
                'name': imgfile,
                'mimeType': mime
            },
            media_body=MediaFileUpload(imgfile, mimetype=mime, resumable=True)
        ).execute()

        downloader = MediaIoBaseDownload(
            result,
            self.service.files().export_media(
                fileId=res['id'], mimeType="text/plain")
        )

        done = False
        while not done:
            status, done = downloader.next_chunk()

        self.service.files().delete(fileId=res['id']).execute()
        return result.getvalue().decode('utf-8')


if __name__ == "__main__":
    drive = Image_to_Text()
    result = drive.image2text("../assets/electromagnetics.png")
    print(result)
