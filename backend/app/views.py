from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets, permissions
from .models import Books
from .serialize import BooksSerializer

# Create your views here.

#the response of the views can be obtained from the url: https://localhost/api/books

class BooksViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class =  BooksSerializer
    
