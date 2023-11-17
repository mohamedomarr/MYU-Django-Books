from rest_framework import serializers
from .models import Author, Book, Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        
class BookSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

       
class BookSerializer(serializers.ModelSerializer):
    review_book = ReviewSerializer(many=True)
    class Meta:
        model = Book
        fields = '__all__'
        
         
class AuthorSerializer(serializers.ModelSerializer):
    book_author = BookSerializerList(many=True)
    class Meta:
        model = Author
        fields = '__all__'