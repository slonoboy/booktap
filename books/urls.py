from unicodedata import name
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import*

urlpatterns=[
    path('profil_unik/',profil_unik,name='profil_unik'),
    path('ranking/',ranking,name='ranking'),
    path('profile/',profile,name='profile'),
    path('',signin,name='signin'),
    path('signup/',signup,name='signup'),
    path('books/<int:id>',books,name='books'),
    path('korzina/',korzina,name='korzina'),
    path('list/',listq,name='list'),
    path('main/',main,name='main'),
    path('payment/',payment,name='payment'),
    path('payment_info/',payment_info,name='payment_info'),
    path('zakazy/',zakazy,name='zakazy'),
    path('reg_book/',reg_book,name='reg_book'),
    path('moderator/',moderator,name='moderator'),

    path('profilenu/',profilenu,name='profilenu'),

    path('profile_unik_enu/', profile_unik_enu, name = 'profil_unik_enu')

    # path('device/<int:assetid>/',checker)
] 