import datetime, json

def saveOptions():
    date = datetime.datetime.now()
    inputDate = list(input(f'Enter date DD-MM-YYYY today {date.strftime("%d")}-{date.strftime("%m")}-{date.year} -> ').split('.'))

    rover = input('Choose rover name (Curiosity/Opportunity/Spirit) -> ')
    options = {'date': inputDate, 'rover': rover}
    json.dumps(options)
    with open('functions/options.json', 'w+') as f:
        json.dump(options, f)
        f.close()
def loadOptions():
    file = open("functions/options.json", "r")
    options = json.load(file)
    file.close()
    return options