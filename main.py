import datetime
import os
from functions import options_functions, downloader

API_KEY = 'zcf5CJHbY1x6A65XOCONcUPBDIohHZZqJEew9KDl' #Your api key

while True:
    print("""Options: 
        <- create (Creating index.html file)
        <- delete (Deleting index.html file)
        <- options (Choosing date for image gallery and rover)
        <- download (Downloading images)
        """)
    option = input("-> ")

    if(option == 'create'):
        html_doc = """<html>
            <head>
                <title>Mars</title>
            </head>
            <body>
            </body>
    </html>
        """
        file = open('index.html', 'w+')
        file.write(html_doc)
        file.close()
        print('File created successful')

    if(option == 'delete'):
        if os.path.exists('functions/index.html'):
            os.remove('functions/index.html')
            print('File deleted successful')
        else:
            print('The file does not exist''')

    if(option == 'download'):
        options = options_functions.loadOptions()
        date = datetime.datetime(int(options['date'][2]), int(options['date'][1]), int(options['date'][0]))
        rover = options['rover']
        data = downloader.getImage(date, rover, API_KEY)
        downloader.createGallery(data)
        print('Take a look at index.html')

    if(option == 'options'):
        options_functions.saveOptions()
    else:
        print("Command doesn't exist")



