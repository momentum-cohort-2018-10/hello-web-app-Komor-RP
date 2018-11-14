from django.shortcuts import render
from Library.models import Book


def index(request):
    books = Book.objects.all()
    return render(request, 'index.html', {
        'books': books
    })


def book_detail(request, slug):
    book = Book.objects.get(slug=slug)

    return render(request, 'books/book_detail.html', {
        'book': book,
    })
