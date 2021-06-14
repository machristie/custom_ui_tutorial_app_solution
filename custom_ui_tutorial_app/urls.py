
from django.urls import path

from . import views

app_name = 'custom_ui_tutorial_app'
urlpatterns = [
    path('home/', views.home, name='home'),
    path('hello/', views.hello_world, name="hello_world"),
    path('languages/', views.languages, name="languages"),
]
