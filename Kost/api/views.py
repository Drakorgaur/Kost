#dango
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404
from django.contrib.auth.models import User
#REST
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
#api
from api.models import Snippet
from api.serializers import SnippetSerializer, UserSerializer
from api.permissions import IsAdmin
#models+


class SnippetAPI():
    class SnippetList(APIView):
        permission_classes = [IsAdmin]
        required_groups = {
         'GET': ['Admin',],
         'POST': ['Admin',],
     }

        def get(self, request, format=None):
            snippets = Snippet.objects.all()
            serializer = SnippetSerializer(snippets, many=True)
            return Response(serializer.data)

        def post(self, request, format=None):
            serializer = SnippetSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    class SnippetDetail(APIView):
        permission_classes = [IsAdmin]
        required_groups = {
         'GET': ['Admin',],
         'POST': ['Admin',],
     }

        def get_object(self, pk):
            try:
                return Snippet.objects.get(pk=pk)
            except Snippet.DoesNotExist:
                raise Http404

        def get(self, request, pk, format=None):
            snippet = self.get_object(pk)
            serializer = SnippetSerializer(snippet)
            return Response(serializer.data)

        def put(self, request, pk, format=None):
            snippet = self.get_object(pk)
            serializer = SnippetSerializer(snippet, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        def delete(self, request, pk, format=None):
            snippet = self.get_object(pk)
            snippet.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class UserAPI():
    class UserList(APIView):
        permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                      IsAdmin]

        def get(self, request, format=None):
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)

        def post(self, request, format=None):
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    class UserDetail(APIView):
        permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                      IsAdmin]

        def get_object(self, username_):
            try:
                return User.objects.get(username=username_)
            except User.DoesNotExist:
                pass

        def get(self, request, username_, format=None):
            user = self.get_object(username_)
            serializer = UserSerializer(user)
            return Response(serializer.data)

        def put(self, request, username_, format=None):
            user = self.get_object(username_)
            serializer = UserSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        def delete(self, request, username_, format=None):
            user = self.get_object(username_)
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
