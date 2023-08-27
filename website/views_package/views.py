from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie
import os
import random
import json
import xmltodict
from . import createjson

# Create your views here.
def parseXML(root,dir,file):
    #open file
    try:
        with open(os.path.join(root,dir,file),"r",encoding='UTF-8') as XMLfile:
        #read onto a var
            XMLcontent = XMLfile.read()
            #parse to a dict
            XMLdict = xmltodict.parse(XMLcontent,encoding="utf-8")
        return XMLdict
    except FileNotFoundError:
        print("There is no XML file", os.path.join(root,dir,file))
        return None

def parseJSON(root,dir,file):
    try:
        with open(os.path.join(root,dir,file),'r') as json_file:
            data = json.load(json_file)

        return data
    except FileNotFoundError:
        print("There is no JSON file", os.path.join(root,dir,file))
        return None
    except json.JSONDecodeError as e:
        print("json parse error")
        return None
    
def createDict():
    path = 'static\BOOK'
    bookDict = {}
    num = 0
    for root, dirs, files in os.walk(path):  
        for dir in dirs:
            modifyDir = dir.replace('[',"").replace(']',"").replace('_', " ").replace('-'," ")
            imagesArray = []
            infoDict = {}           
            for files in os.listdir(os.path.join(root,dir)):                       
                if files.endswith(('.jpg', '.png')):
                    imagesArray.append(files)
                if files.endswith(('.xml')):
                    infoDict = parseXML(root,dir,files, modifyDir)
                if files.endswith(('.json')):
                    infoDict = parseJSON(root,dir,files)           
            if len(imagesArray) != 0:
                bookDict[num]=imagesArray
                bookDict[num].append(infoDict)
                bookDict[num].append(modifyDir)
                dir = dir.replace('#','%23')
                bookDict[num].append(os.path.join(root,dir))               
                num+=1

    return bookDict

def home(request):
    bookDict = createDict()
    return render(request,'home.html',{'bookDict': bookDict})

def content(request, selection):
    bookNum = int(selection)
    bookDict = createDict()
    images={
        "0":bookDict[bookNum]
    }
    rootDir = {
        "0": bookDict[bookNum].pop()
    }
    Dir = {
        "0": bookDict[bookNum].pop()
    }
    infoDict = {
        "0": bookDict[bookNum].pop()
    }
    selection = {
        "0":bookNum
    }
    return render(request,'content.html',{'images':images,'root':rootDir,'dir':Dir, 'selection':selection,'infoDict':infoDict})

def read(request, selection,pageNum):
    bookNum = int(selection)
    pageNum = int(pageNum)
    bookDict = createDict()
    image = bookDict[bookNum][pageNum]
    images={
        "0":bookDict[bookNum]
    }
    rootDir = {
        "0": bookDict[bookNum].pop()
    }
    Dir = {
        "0": bookDict[bookNum].pop()
    }
    infoDict = {
        "0": bookDict[bookNum].pop()
    }
    selection = {
        "0":bookNum
    }
    pageNum = {
        "0":pageNum-1,
        "1":pageNum+1,
        "total_pages" : len(images['0'])-1,
        "current_page" : pageNum
    }
    image = {
        "0": image
    }
    return render(request,'read.html',{'images':images,'root':rootDir,'dir':Dir, 'selection':selection, 'pageNum':pageNum, 'image':image})

@ensure_csrf_cookie
def search(request):
    return render(request, 'search.html')

@ensure_csrf_cookie
def search_results(request, letter):
    bookDict = createDict()
    modifiedDict = {}
    for key,value in bookDict.items():
        dir = value[-2]
        if str(letter) == dir.lower()[0]:
            modifiedDict[key] = value
    return render(request, 'search_results.html', {'bookDict': modifiedDict})


def quicksearch (request):
    bookDict = createDict()
    input = request.POST['input']
    searchDict = {}
    for key,value in bookDict.items():
        dir = value[-2]
        if input in dir.lower():
            searchDict[key] = value
    return render(request, 'quicksearch.html', {'searchDict': searchDict})

def randomsearch(request):
    bookDict = createDict()
    randomDict = {}
    keys = list(bookDict.keys())
    random.shuffle(keys)
    for key in keys:
        randomDict[key] = bookDict[key]

    return render(request, 'randomsearch.html',{'randomDict':randomDict})
