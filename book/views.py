from django.shortcuts import render

from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import generics
from .serializers import AuthorSerializer, BookSerializer, ReviewSerializer
from .models import Author, Book

# Create your views here.
class AuthorListAPI(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    search_fields = ['$name', '=birth_date']
    filterset_fields = ['name', 'birth_date']
    ordering_fields = ['name', 'birth_date']

class AuthorDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookListAPI(generics.ListCreateAPIView): 
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    search_fields = ['$title', '=publication_date', '=price', 'genre', '$author__name']
    filterset_fields = ['publication_date', 'price', 'genre']
    ordering_fields = ['title', 'publication_date', 'price', 'genre', 'author__name']

class BookDetailAPI(generics.RetrieveUpdateDestroyAPIView): 
    queryset = Book.objects.all()
    serializer_class = BookSerializer