from django.shortcuts import render

from rest_framework import generics
from .serializers import AuthorSerializer, BookSerializer, ReviewSerializer
from .models import Author, Book

# Create your views here.
class AuthorListAPI(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookListAPI(generics.ListCreateAPIView): 
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailAPI(generics.RetrieveUpdateDestroyAPIView): 
    queryset = Book.objects.all()
    serializer_class = BookSerializer