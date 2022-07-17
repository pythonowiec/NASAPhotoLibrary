import bs4
import requests

def getImage(date, rover, API_KEY):
    print(f'https://api.nasa.gov/mars-photos/api/v1/rovers/{rover}/photos?earth_date={date.year}-{date.strftime("%m")}-{date.strftime("%d")}&api_key={API_KEY}')
    r = requests.get(f'https://api.nasa.gov/mars-photos/api/v1/rovers/{rover}/photos?earth_date={date.year}-{date.strftime("%m")}-{date.strftime("%d")}&api_key={API_KEY}')
    data = r.json()
    return data

def createGallery(data):
    file = open('index.html', 'r')
    soup = bs4.BeautifulSoup(file.read(), features="html.parser")

    for photo in data["photos"]:
        new_image = soup.new_tag('img', src=photo["img_src"], width=1000, height=1000)

        soup.body.append(new_image)

    file = open('index.html', 'w')
    file.write(str(soup))
    file.close()

    print('Something went wrong')



