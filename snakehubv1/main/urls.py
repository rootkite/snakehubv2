from django.urls import path
from main import views

app_name = 'main'

urlpatterns = [
    
    path('', views.index,name='index'),
    path('home/', views.index,name='index'),
    path('signup/', views.registernl,name='registernl'),
    path('users/', views.newsletter_users,name='users'),
    path('about/', views.about,name='about'),
    path('login/', views.user_login,name='user_login'),
    path('mainsignup/', views.mainregister,name='mainregister'),
    path('logout/',views.user_logout,name='user_logout'),
    path('special/',views.specialcontent,name='specialcontent'),


    
    
]