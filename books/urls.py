from django.urls import path

from .views import*

urlpatterns=[
    path('profil_unik/',profil_unik,name='profil_unik'),
    path('ranking/',ranking,name='ranking'),
    path('profile/',profile,name='profile'),
    path('signin/',signin,name='signin'),
    path('signup/',signup,name='signup'),
    path('books/',books,name='books'),
    path('korzina/',korzina,name='korzina'),
    path('list/',listq,name='list'),
    path('',main,name='main'),
    path('payment/',payment,name='payment'),
    path('zakazy/',zakazy,name='zakazy'),
    # path('device/<int:assetid>/',checker)
]