from django.urls import path
from . import views

urlpatterns=[
    path('menu/',views.menu,name="menu"),
    path('',views.index,name='index'),
    path('create',views.create,name='create'),
    path('read',views.read,name='read'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('edit/update/<int:id>',views.update,name='update'),

]