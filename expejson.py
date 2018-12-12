import json

def writeToJSONFile(path, fileName, data):
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'a+') as fp:
        json.dump(data, fp)


# Example
data = {}
data['id'] =   raw_input('Enter id :')
data['name'] = raw_input('Enter name :')
data['cost'] = raw_input('Enter cost :')
data['date'] = raw_input('Enter date :')

writeToJSONFile('./','expence',data)
