from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Post
from .serializers import PostSerializer


class PostAPI(APIView):
    authentication_classes = [

    ]
    permission_classes = [
        
    ]
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        data = request.data
        serializer = PostDetailAPI(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetailAPI(APIView):
    def get(self, request, id):
        try:
            post = Post.objects.get(id=id)
            serializer = PostSerializer(post)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({"Error": "The post doesn't exist"}, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, id):
        try:
            post = Post.objects.get(id=id)
            serializer = PostSerializer(instance=post, data=request.data)
            if serializer.is_valid():
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"Error": "The post doesn't exist"}, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        try:
            post = Post.objects.get(id=id)
            post.delete()
        except:
            return Response({"Error": "The post doesn't exist"}, status=status.HTTP_400_BAD_REQUEST)