from .models import Song
from .serializers import SongSerializer
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from django.core.cache import cache

class SongList(APIView):
    def get(self, request, format=None):
        song = cache.get_or_set('song',Song.objects.all())
        songSerializer = SongSerializer(song, many=True)
        return Response(songSerializer.data)
    def post(self, request,format=None):
        songSerializer = SongSerializer(data=request.data)
        if songSerializer.is_valid():
            cache.delete('song')
            songSerializer.save()
            return Response(songSerializer.data, status=status.HTTP_201_CREATED)
        return Response(songSerializer.errors, status=400)

class SongDetail(APIView):
    def get_object(self,id):
        try:
            return Song.objects.filter(id=id)
        except Song.DoesNotExist:
            raise Http404
    def get(self,request,id ,format=None):
        song=self.get_object(id)
        if 0 == len(song):
            return Response({"msg":"this number not exist."},status=400)
        songSerializer=SongSerializer(song, many=True)
        return Response(songSerializer.data, status=202)
    def put(self,request,id ,format=None):
        song=self.get_object(id)
        if len(song) == 0:
            return Response({"msg":"this number not exist."}, status=400)
        song.title=request.data['title']
        song.singer=request.data['singer']
        song.producer=request.data['producer']
        song.entertainment=request.data['entertainment']
        song.tracknum=request.data['tracknum']
        songSerializer = SongSerializer(song, data=request.data)
        songSerializer.is_valid()
        songSerializer.save()
        cache.delete('song')
        cache.delete(f'song:{id}')
        return Response(songSerializer.data, status=204)
    def delete(self,request,id, format=None):
        song=self.get_object(id)
        if 0 == len(song):
            return Response({"msg":"this number not exist."}, status=400)
        cache.delete(f'song:{id}')
        cache.delete('song')
        song.delete()
        return Response(status=204)
    