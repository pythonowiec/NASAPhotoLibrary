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

    elif(option == 'delete'):
        if os.path.exists('index.html'):
            os.remove('index.html')
            print('File deleted successful')
        else:
            print('The file does not exist''')

    elif(option == 'download'):
        options = options_functions.loadOptions()
        date = datetime.datetime(int(options['date'][2]), int(options['date'][1]), int(options['date'][0]))
        rover = options['rover']
        data = downloader.getImage(date, rover, API_KEY)
        downloader.createGallery(data)
        print('Take a look at index.html')

    elif(option == 'options'):
        op = options_functions.loadOptions()
        print('Your options: ')
        print(f'<-  {op["date"][0]}.{op["date"][1]}.{op["date"][2]}')
        print('<- ', op['rover'])
        options_functions.saveOptions()
        print('Saved')
    else:
        print("Command doesn't exist")



