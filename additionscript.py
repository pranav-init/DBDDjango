import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE','demo_blog.settings')

import django
django.setup()

import re

from demo.models import Nice

def nuSorter(stro):
    return int(stro) if stro.isdigit() else stro
def nuKeyGen(stro):
    return [ nuSorter(c) for c in re.split('(\d+)',stro) ]

def populate():
    lis = []
   
    path = 'D:/#1/edited/'
    files = os.listdir(path)

    for i in files:
        if i[-4:]==".txt":
            lis.append(i)
    
    lis.sort(key=nuKeyGen)
 
    for i in lis:
        title = i[:-4]
        tempfile = open(path+i,"r",encoding="utf8",errors="ignore")
        content = tempfile.read()
        webpg = Nice.objects.get_or_create(niceTitle=title,niceContent=content,niceAuthor='Moderator')[0]



if __name__ == '__main__':
    print("Populating Script....")
    populate()
    print("Population Complete!")