from django.urls import path

from .views import*

urlpatterns=[
    path('profil_unik/',profil_unik,name='profil_unik'),
    path('ranking/',ranking,name='ranking'),
    path('profile/<int:assetid>',profile,name='profile'),
    path('',signin,name='signin'),
    path('signup/',signup,name='signup'),
    path('books/',books,name='books'),
    path('korzina/',korzina,name='korzina'),
    path('list/',listq,name='list'),
    path('main/',main,name='main'),
    path('payment/',payment,name='payment'),
    path('zakazy/',zakazy,name='zakazy'),
    path('reg_book/',reg_book,name='reg_book'),
    path('moderator/',moderator,name='moderator'),
    # path('device/<int:assetid>/',checker)
]