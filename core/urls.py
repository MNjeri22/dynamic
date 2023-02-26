
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', views.projects, name='projects'),
    path('cv/', views.cv, name='cv'),
    path('hire-me/', views.hireme, name='hireme'),
]

   