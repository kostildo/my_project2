from django.conf.urls import url
from django.urls import path
from riddles import views

app_name = 'riddles'

urlpatterns = [
    url(r'^$', views.index, name='my_site'),
    path('create/', views.create),
    path('edit/<int:id>/', views.edit),
    path('delete/<int:id>/', views.delete),
    path('', views.index),
]