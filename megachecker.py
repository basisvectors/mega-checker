import re
from random import randint
regex = r"https:\/\/mega\.nz\/(file|folder)\/[\s\S]*#[\s\S]*"
api = 'https://g.api.mega.co.nz'

def isUrlValid(url):

    match = re.match(regex, url)
    if not match and match.group() == url:
        return False
    urltype = url.split("/")[3]
    id = url.split("/")[4].split("#")[0]
    
    if (urltype == 'folder'):
        data = { "a": "f", "c": 1, "r": 1, "ca": 1 }
    else:
        data = { "a": 'g', "p": id }
    params = {
    'id': ''.join(["{}".format(randint(0, 9)) for num in range(0, 10)]),
    'n': id
    }

    response = requests.post('https://g.api.mega.co.nz/cs', params=params, data=data)

    return response.json() == -2
