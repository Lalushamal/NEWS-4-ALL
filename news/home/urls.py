from django.urls import path
from . import views


urlpatterns=[ 

    path('',views.index,name='index'),
    path('category',views.category,name='category'),
    path('contact',views.contact,name='contact'),
    path('sports',views.sports,name='sports'),
    path('technology',views.technology,name='technology'),
    path('business',views.business,name='business'),
]