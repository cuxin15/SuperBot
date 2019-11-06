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
    print('Query:', query)
    out = []
    for i in iterable:
        if filtor(i, query='') == True:
            out.append(i)
    return out


def isUrlImageJPG(url, query=''):
    # ../url/image.jpg
    print('isUrlImageJPG', query)
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


def iDontKnowItsName(url, query):
    a = isUrlImagePNG(url, query)
    b = inQuery(url, query)
    print('a', a)
    print('b', b)
    return a == b

# STRING


def toLowcase(string):
    return unidecode.unidecode(string).lower()


# MATH
def fac(x):
    """Factorial"""
    out = 1
    lim = 1
    while lim <= x:
        out *= lim
        lim += 1
    return out


def fibonacci(n):
    """Flowers and something like that. Dãy Fibonacci là dãy vô hạn các số tự nhiên bắt đầu bằng hai phần tử 0 và 1 hoặc 1 và 1, các phần tử sau đó được thiết lập theo quy tắc mỗi phần tử luôn bằng tổng hai phần tử trước nó."""
    from math import sqrt
    return int(((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5)))

if __name__ == '__main__':
    x = fibonacci(10)
    y = fac(0)

    print(x, y)
