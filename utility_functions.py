import unidecode

# UTILITY FUNCTION
def find(finder, iterable):
    for i in iterable:
        if finder(i) == True:
            return i


def filter(filtor, iterable, *args):
    out = []
    for i in iterable:
        if filtor(i, *args) == True:
            out.append(i)
    return out


def isUrlImageJPG(url):
    # ../url/image.jpg
    split_url = url.split('/')
    if '.jpg' in split_url[-1].lower():
        return True


def isUrlImagePNG(url):
    split_url = url.split('/')
    if '.png' in split_url[-1].lower():
        return True


def isMaxPixel(url):
    split_url = url.split('/')
    if '.png' in split_url[-1].lower():
        return True


def inQueryAndPNG(url: str, *args):
    if ' '.join(*args) in url.lower() and isUrlImagePNG(url):
        return True


def inQuery(url: str, *args):
    # X:\github_truongaxin123\XXX-bot\discord_image\Ad-tech_London_2010_%282%29.JPG
    split_path = url.split('/')
    split_name = split_path[-1].split('-')
    query = split_name[0]
    if query == ' '.join(args):
        return True


def toLowcase(string):
    return unidecode.unidecode(string).lower()
