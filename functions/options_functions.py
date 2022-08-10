import datetime, json

def saveOptions():
    date = datetime.datetime.now()
    op = loadOptions()
    inputDate = list(input(f'Enter date DD.MM.YYYY today {date.strftime("%d")}.{date.strftime("%m")}.{date.year} for skip press enter -> ').split('.'))
    rover = input('Choose rover name (Curiosity/Perseverance/Opportunity/Spirit) for skip press enter -> ')

    if (inputDate == ['']):
        inputDate = [op['date'][0], op['date'][1], op['date'][2]]
    if(rover == ''):
        rover = op['rover']

    options = {'date': inputDate, 'rover': rover}
    json.dumps(options)
    with open('functions/options.json', 'w+') as f:
        json.dump(options, f)
        f.close()
def loadOptions():
    try:
        file = open("functions/options.json", "r+")
        options = json.load(file)
        file.close()
        return options
    except:
        file = open("functions/options.json", "w+")
        options = {'date': [], 'rover': ''}
        json.dump(options, file)
        file.close()

