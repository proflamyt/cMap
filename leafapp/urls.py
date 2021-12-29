from django.urls import path
from .views import display, index, store_points, home

urlpatterns =[

path('map/<int:pk>', index, name='index'),
path('', home, name="home"),
path('points/<str:novel>/<str:type>',display, name='points'),
path('store/<int:pk>', store_points, name='store'),

]