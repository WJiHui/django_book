from django.shortcuts import render
from django.http import HttpResponse
from books.models import Book


# Create your views here.

# http://127.0.0.1:8000/books/search/
def search(request):
    error = None
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = 'Enter a search term'
        elif len(q) > 20:
            error = 'Please enter at most 20 characters.'
        else:
            books = Book.objects.filter(title__icontains=q)
            return render(request, 'books/search_result.html', {'books': books, 'query': q})
    return render(request, 'books/search_form.html', {'error': error})


# http://127.0.0.1:8000/wjh/books/
def home(request, username):
    return HttpResponse("This is %s'book home" % username)


# http://127.0.0.1:8000/wjh/books/xiyouji/page1/
def book(request, username, title, num):
    return HttpResponse("%s'book-%s-%s" % (username, title, num))