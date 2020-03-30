from django.contrib import admin
from django.urls import path
from django.urls import include
from. import views
app_name="news"
urlpatterns = [
    path('', views.ForeignView.as_view(), name="index"),
    path('news/<str:country_name>', views.IndexView.as_view(), name='f-news'),
    path('news/<str:country_name>/top', views.TopIndexView.as_view(), name='f-news-top'),
]