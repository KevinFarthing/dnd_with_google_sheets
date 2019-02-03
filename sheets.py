from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from chargen import getstats

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
# SAMPLE_SPREADSHEET_ID = '1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms'
nazhmor_sheet = '1T_gOY0QAeDSZLBQH5wj6TPjHsZQYQyhwStvY4B3hHck'
mura_sheet = '1sHELLF_ThImMdajT7GgHS7jxBOnImyjUyP0YJQJcwXw'
dachenmaz_sheet = '1-_5E_GhfDcLKinupencl-GoQhLoQvOZhkHQt-m5vVVo'
vezhek_sheet = '1Mr20d8hX8QlsWTIkpkEtsL3nxA9Vv6AMc6Op22TW4gI'
character_sheets = [nazhmor_sheet,mura_sheet,dachenmaz_sheet,vezhek_sheet]

stat1 = 'ABILITY SCORES!B7'
stat2 = 'ABILITY SCORES!B11'
stat3 = 'ABILITY SCORES!B15'
stat4 = 'ABILITY SCORES!B19'
stat5 = 'ABILITY SCORES!B23'
stat6 = 'ABILITY SCORES!B27'
sheetstats = [stat1,stat2,stat3,stat4,stat5,stat6]
# SAMPLE_RANGE_NAME = 'Class Data!A2:E'

def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
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
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    for character_sheet in character_sheets:
        stats = getstats()
        print(stats)
        for i in range(6):
            result = sheet.values().update(
                spreadsheetId=character_sheet,
                range = sheetstats[i],
                valueInputOption = 'USER_ENTERED',
                body = {'values': [[stats[i]]]}
            ).execute()
            # print('{0} cells updated.'.format(result.get('updatedCells')))

    # result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
    #                             range=SAMPLE_RANGE_NAME).execute()
    # values = result.get('values', [])

    # if not values:
    #     print('No data found.')
    # else:
    #     print('Name, Major:')
    #     for row in values:
    #         # Print columns A and E, which correspond to indices 0 and 4.
    #         print('%s, %s' % (row[0], row[4]))

if __name__ == '__main__':
    main()