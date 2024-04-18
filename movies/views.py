from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from movies.models import Movie
from movies.serializer import MoviesSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication


class MovieView(APIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def post(self, request: Request):
        serializer = MoviesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data, status.HTTP_201_CREATED)
    
    def get(self, request: Request):
        movies = Movie.objects.all()
        return Response(MoviesSerializer(movies, many=True).data, status.HTTP_200_OK)
    