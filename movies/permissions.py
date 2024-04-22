from rest_framework import permissions
from rest_framework.views import Request, View
from movies.models import Movie


class IsBookOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: Movie):
        return obj.added_by == request.user
    
