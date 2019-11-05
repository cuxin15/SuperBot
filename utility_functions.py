import imgkit
import unidecode

# UTILITY FUNCTION
def find(finder, iterable):
    for i in iterable:
        if finder(i) == True:
            return i


def filter(filtor, iterable=[], query=''):
    query = query.lower()
    query = unidecode.unidecode(query)
    query = ''.join(query.split(' '))
    print('Query:',query)
    out = []
    for i in iterable:
        if filtor(i, query='') == True:
            out.append(i)
    return out


def isUrlImageJPG(url, query=''):
    # ../url/image.jpg
    print('isUrlImageJPG',query)
    split_url = url.split('/')
    if '.jpg' in split_url[-1].lower():
        return True

def isUrlImagePNG(url, query=''):
    # ../url/image.jpg
    split_url = url.split('/')
    if '.png' in split_url[-1].lower():
        return True

def inQuery(url, query):
    print('inQuery', query)
    print('inQuery url', url)
    # X:\github_truongaxin123\bot\discord_image\example.JPG
    split_path = url.split('/')
    split_name = split_path[-1].split('-')
    split_query = split_name[0]
    if split_query == query:
        return True

def iDontKnowItsName(url,query):
    a = isUrlImagePNG(url, query)
    b = inQuery(url,query)
    print('a',a)
    print('b',b)
    return a==b

def toLowcase(string):
    return unidecode.unidecode(string).lower()


imgkit.from_file('widget-weather.html', 'out.jpg')

