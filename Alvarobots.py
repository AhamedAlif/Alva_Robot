import requests
import sys
import re

class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    blue = "\033[34m"

def main():  
    print("\033[34m" + """
   _____  .__ ___.         __________      ___.           __   
  /  _  \ |  |\_ |__ _____ \______   \ ____\_ |__   _____/  |_ 
 /  /_\  \|  | | __ \\__  \ |       _//  _ \| __ \ /  _ \   __\\
/    |    \  |_| \_\ \/ __ \|    |   (  <_> ) \_\ (  <_> )  |  
\____|__  /____/___  (____  /____|_  /\____/|___  /\____/|__|  
        \/         \/     \/       \/           \/             
\033[0m""")

    host =  input(bcolors.ENDC + "Enter the URL: ")

    print('Trying to fetch robots.txt from the supplied URL')
    robotsURL = host + '/robots.txt'
    fakeUAHeader = {'User-Agent': 'Googlebot/2.1'}  # spoof Googlebot UA

    try:
        r = requests.get(robotsURL, headers=fakeUAHeader)
    except requests.RequestException as e:
        print('Invalid URL supplied or error during request:', e)
        sys.exit()

    robotsPaths = re.findall(r'Disallow: (.*)', r.text)
    robotsPaths = list(set(robotsPaths))  # remove duplicates

    for path in robotsPaths:
        pathURL = host + path
        try:
            r = requests.get(pathURL)
            finalResult = (
                f"{pathURL} {r.status_code} {r.headers.get('content-length', '')} {bcolors.ENDC}"
            )
            if r.status_code == 200:
                print(bcolors.GREEN + finalResult)
            elif r.status_code in [404, 403]:
                print(bcolors.RED + finalResult)
            elif r.status_code in [500, 302]:
                print(bcolors.YELLOW + finalResult)
        except requests.RequestException:
            print('Failed to fetch URL:', pathURL)

if __name__ == '__main__':
    main()
