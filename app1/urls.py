from django.urls import path
from app1 import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.Test.first_page, name='Home Page'),
    path('second', views.Test.second_page, name='Second Page'),
    path('save_model', views.Test.save_my_model, name='Save Model'),
    path('delete_model/<int:pk>', views.Test.delete_my_model, name='Delete Model Item'),
    path('edit_model/<int:pk>', views.Test.edit_my_model, name='Edit Model Item'),
    path('update_model', views.Test.update_my_model, name='Update Model Item'),
    path('parser', views.myparser, name='Parser Page'),
    path('parser_account', csrf_exempt(views.enter_account), name='Parser Page'),
    path('movies', views.getMovies),
]