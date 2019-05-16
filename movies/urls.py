from django.urls import path
from . import views
app_name="movies"

urlpatterns =[
    path('', views.main, name="main"),
    path('moviePickUp/', views.moviePickUp),
    path('search/', views.search, name="search"),
    path('<int:id>/', views.detail, name="detail"),
    path('<int:id>/comment/create',views.commentCreate, name="commentCreate"),
]