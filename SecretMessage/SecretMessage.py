#   PROJECT : Secret Message
#   DESCRIPTION :  Using a Google Document URL as the input, Reveal and display the Secret Message
#   SPECIFICATION
#   =============
#   1) Google Document - contains a table with 3 columns these are x-coordinate, Character, y-coordinate
#   2) Get The Data from the web site using the URL.
#   3) Store the Data in a Dictionary using the coordinates
#   4) Print the secret message from the Dictionary  
#
#####################################################

from tarfile import NUL

#	Entry Method call using the Google Document URL 
def showMessage(URL): 
  printSecretMessage(parseGoogleDocData(getData(URL)))

# Using the URL Compiles and returns the Google Doc Data  
def getData(URL):
    from bs4 import BeautifulSoup
    import requests

    # Fetch the document content
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, "html.parser")
    docData = ""
    if response.status_code == 200:
        lines = soup.find_all(class_="c1") #Change class name to match yours 
        count=0
        for line in lines[2:]:
            val = line.text.strip()            
            if val == "" or val is NUL:
                continue
            elif count in (0, 1):
                docData += val + ", "
                count += 1
            else:
                docData += val + "\n"
                count = 0
    else:
        print(f"Error fetching document: {response.status_code}")
    
    
    return docData

#	The Dictionary is created & Populated
def parseGoogleDocData(docData):
    lines = docData.strip().split('\n')		# Split docData into lines
    message = {}		# Create empty Dictionary

  # Populates the grid array as per the data from site
    for line in lines[1:]:  # Skips the first line then iterates through the Secret Message Data
        x, char, y = line.split(', ')
        message[int(x), int(y)] = char
    return message

#	Displays the Secret Message	from the Dictionary
def printSecretMessage(message):
    # Determine the Message
    maxX = max(coord[0] for coord in message)
    maxY = max(coord[1] for coord in message)
    # Print the Secret Message
    for y in range(maxY+1):
        print(''.join(message.get((x, y), ' ') for x in range(maxX+1)))

showMessage('https://docs.google.com/document/d/e/2PACX-1vSHesOf9hv2sPOntssYrEdubmMQm8lwjfwv6NPjjmIRYs_FOYXtqrYgjh85jBUebK9swPXh_a5TJ5Kl/pub')
