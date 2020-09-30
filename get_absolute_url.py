def get_absolute_url(url, *args, **kwargs):
    adress = url
    for arg in args:
        adress += '/' + arg
    adress += '?'
    for k, v in kwargs.items():
        adress += k + '=' + v + '&'
    adress = adress[:-1]
    return adress


print(get_absolute_url('www.yandex.ru', 'posts', 'news', id='24', author='admin'))
print(get_absolute_url('www.google.com', 'images',
                       id='24', category='auto', color='red', size='small'))
