import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE','demo_blog.settings')

import django
django.setup()

import re


from demo.models import Figure

def nuSorter(stro):
    return int(stro) if stro.isdigit() else stro
def nuKeyGen(stro):
    return [ nuSorter(c) for c in re.split('(\d+)',stro) ]

path = 'D:/#1/images/'
files = os.listdir(path)
files.sort(key=nuKeyGen)


for i in files:
    currentTitle = i.replace(".jpg","")
    currentImage = path+i
    webpg = Figure.objects.get_or_create(figTitle=currentTitle,figImage=currentImage)[0]
