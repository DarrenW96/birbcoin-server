from django.http import HttpResponse
from django.template import loader
from flickrapi import FlickrAPI

api_key = u'77c9851c6eb96b6c553d509b4ea7e9e9'
api_secret = u'72461c990fa993a8'


def pics(request):
    flickr = FlickrAPI(api_key, api_secret, format='parsed-json')

    extras = 'url_m'
    myphotos = flickr.photos.search(user_id='140828067@N04', per_page=10, extras=extras)
    template = loader.get_template('myphotos.html')

    total = int(myphotos['photos']['total'])
    photos = []
    print(total)
    for i in range(0, 10):
        photos.append(myphotos['photos']['photo'][i]['url_m'])

    context = {
        'photos': photos,
    }

    return HttpResponse(template.render(context, request))

