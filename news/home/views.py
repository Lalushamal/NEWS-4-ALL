from django.shortcuts import render
from django.http import HttpResponse
import requests


def index(request):
    response = requests.get('https://inshorts.deta.dev/news?category=sports')
    response1 = requests.get('https://inshorts.deta.dev/news?category=technology')
    response2 = requests.get('https://inshorts.deta.dev/news?category=business')
    response3 = requests.get('https://inshorts.deta.dev/news?category=entertainment')

    posts = response.json()
    posts1 = response1.json()
    posts2 = response2.json()
    posts3 = response3.json()
    data = posts['data']
    data1 = posts1['data']
    data2 = posts2['data']
    data3 = posts3['data']
    return render(request,'index.html',{'posts': data, 'posts1':data1, 'posts2':data2, 'posts3':data3})

def category(request):
    response = requests.get('https://inshorts.deta.dev/news?category=sports')
    response1 = requests.get('https://inshorts.deta.dev/news?category=technology')
    response2 = requests.get('https://inshorts.deta.dev/news?category=business')
    response3 = requests.get('https://inshorts.deta.dev/news?category=entertainment')

    posts = response.json()
    posts1 = response1.json()
    posts2 = response2.json()
    posts3 = response3.json()
    data = posts['data']
    data1 = posts1['data']
    data2 = posts2['data']
    data3 = posts3['data']
    return render(request,'index.html',{'posts': data, 'posts1':data1, 'posts2':data2, 'posts3':data3})

def contact(request):
    return render(request,'contact.html')    


def sports(request):
    response = requests.get('https://inshorts.deta.dev/news?category=sports')
    posts = response.json()
    data = posts['data']
    
    return render(request,'sports.html',{'posts': data})    

def technology(request):
    response1 = requests.get('https://inshorts.deta.dev/news?category=technology')
    posts1 = response1.json()
    data1 = posts1['data']
    return render(request,'technology.html',{'posts1':data1}) 

def business(request):
    response2 = requests.get('https://inshorts.deta.dev/news?category=business')
    posts2 = response2.json()
    data2 = posts2['data']
    return render(request,'business.html',{'posts2':data2}) 
    
