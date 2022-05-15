from django.shortcuts import render
import random
import pandas
from .models import Photo
source = list(Photo.objects.values('name','img','rating'))
photos = [[item['name'],item['img'],item['rating']] for item in source]
length = int(len(photos))
key=0

def Random_image():
    global source
    image1 = random.choice(source)
    image2 = random.choice(source)
    while(image1 == image2): image2 = random.choice(source)
    return image1,image2

img1, img2 = Random_image()

def NewRating(r1, r2, n):
    exp = (r2-r1)/400.0
    e1 = 1/((10.0**(exp))+1)
    n1 = r1 + 32*(n-e1)
    return int(n1)

def index(request):
    global img1, img2, key
    img1, img2 = Random_image()
    data = {'name1':img1['name'], 'img1':img1['img'], 'rating1':img1['rating'], 'name2':img2['name'], 'img2':img2['img'], 'rating2':img2['rating']}
    key=0
    return render(request, 'index.html',data)

def check(request):
    global img1, img2, key
    if(key==1):
        key=0
        img1, img2 = Random_image()
        data = {'name1': img1['name'], 'img1': img1['img'], 'rating1': img1['rating'], 'name2': img2['name'], 'img2': img2['img'], 'rating2': img2['rating']}
    else:
        key=1
        if request.method == "POST":
            name = request.POST.get('img')
            print(name)
            if(name == img1['img']):
                img1['rating'] = NewRating(img1['rating'], img2['rating'], 1)
                img2['rating'] = NewRating(img2['rating'], img1['rating'], 0)
            elif(name == img2['img']):
                img1['rating'] = NewRating(img1['rating'], img2['rating'], 0)
                img2['rating'] = NewRating(img2['rating'], img1['rating'], 1)
        data = {'name1': img1['name'], 'img1': img1['img'], 'rating1': img1['rating'], 'name2': img2['name'], 'img2': img2['img'], 'rating2': img2['rating']}
    return render(request, 'index.html',data)

def leaderboard(request):
    global photos
    photos = [[item['name'], item['img'], item['rating']] for item in source]
    # {k: v for k, v in sorted(source.items(), key=lambda item: item[2])}

    # d = photos
    d = sorted(photos, key = lambda x: x[2], reverse=True)
    return render(request,'leaderboard.html', {'d':d})