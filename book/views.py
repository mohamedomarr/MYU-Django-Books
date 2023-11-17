from django.shortcuts import render


from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import AuthorSerializer
from .models import Author

# Create your views here.
@api_view(['GET'])
def author_list_api(request):
    authors = Author.objects.all()
    data = AuthorSerializer(authors, many=True).data
    return Response({'authors':data})


@api_view(['GET'])
def author_detail_api(request, id):
    author = Author.objects.get(id=id)
    data = AuthorSerializer(author).data
    return Response({'author':data})