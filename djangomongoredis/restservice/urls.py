from django.urls import path
from .views import SongList, SongDetail
urlpatterns = [
    path('song/',SongList.as_view(),name="song"),
    path('song/<int:id>/',SongDetail.as_view(), name="songdetail"),
]