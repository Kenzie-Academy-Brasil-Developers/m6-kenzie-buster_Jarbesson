from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from movies.models import Movie  
from movies.serializer import MoviesSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import IsAdiminOrReadeOlnly
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination


class MovieView(APIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdiminOrReadeOlnly]

    def post(self, request: Request):
        serializer = MoviesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data, status.HTTP_201_CREATED)
    
    def get(self, request: Request):
        movies = Movie.objects.all()
        query_result = self.paginate_queryset(movies, request, view=self)
        serializer = MoviesSerializer(query_result, many=True)
        return self.get_paginated_response(serializer.data)
    

class MovieDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdiminOrReadeOlnly]

    def get(self, request: Request, movie_id: int):
        movie = get_object_or_404(Movie, pk=movie_id)
        serializer = MoviesSerializer(movie)
    
        return Response(serializer.data, status.HTTP_200_OK)
    
    def delete(self, request: Request, movie_id: int):
        movie = get_object_or_404(Movie, pk=movie_id)
        self.check_object_permissions(request, movie) 
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)