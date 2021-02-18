import requests
import config

AMP_CLIENT_ID = ''
AMP_KEY = ''


	
def listEventTypes():
    url = 'https://api.amp.cisco.com/v1/ABCD'

    # do GET request for the domain status and category
    req = requests.get(url, auth = (AMP_CLIENT_ID, AMP_KEY))

    # error handling if true then the request was HTTP 200, so successful
    if (req.status_code != 200):
        print('An error has ocurred with the following code %s' % req.status_code)
        sys.exit(0)

    output = req.json()
    print (output)


def main():
    # Print the menu
    print('''
            Cisco Secure - List Event Types
                     SRW Blitz, Lab
                   ''')

    listEventTypes()


if __name__ == '__main__':
    main()

