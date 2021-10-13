from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('save', views.save, name='save'),
    path('edit', views.edit, name='edit'),
    path('editform', views.editform, name='editform'),
    path('delete', views.delete,name='delete'),

]