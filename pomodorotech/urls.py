from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('check',views.check,name="check"),
    path('about',views.about,name="about")
]
