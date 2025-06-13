from django.shortcuts import render, HttpResponse
from .models import Todo

# Create your views here.

def todo(request):
    res = Todo.objects.all()
    return HttpResponse(Todo)




'''

for books

 
def get(request):
    books = Books.objects.all()
    return HttpResponse(books)

def getById(request):
    id = request.GET['id']
    books = Books.objects.filter(bookId= id)
    return HttpResponse(books)

def post(request):
    id = request.GET['id']
    name = request.GET['name']
    author = request.GET['author']
    price = request.GET['price']
    isbn = request.GET['isbn']
    
    f= Books(bookId=id, bookName=name, author=author, price=price, isbn=isbn)
    f=f.save()
    return HttpResponse("Saved book details")

def delete(request):
    id = request.GET['id']
    res= Books.Objects.delete(bookId=id)
    return HttpResponse("Deleted Successfully")

def update(request):
    id = request.GET['id']
    f= Books.objects.filter(bookId=id)
    name = request.GET['name']
    author = request.GET['author']
    price = request.GET['price']
    isbn = request.GET['isbn']
    
    f["bookName"]=name
    f["author"]= author
    f["price"] = price
    f["isbn"] = isbn
    f=f.save()
    return HttpResponse("Details updated")
    
    '''