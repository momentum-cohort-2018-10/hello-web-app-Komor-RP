from django.shortcuts import render, redirect
from Library.forms import BookForm
from Library.models import Book
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required
from django.http import Http404


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

@login_required
def edit_book(request, slug):
    book = Book.objects.get(slug=slug)

    if book.user != request.user:
        raise Http404

    form_class = BookForm
    if request.method == 'POST':
        form = form_class(data=request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_detail', slug=book.slug)

    else:
        form = form_class(instance=book)

    return render(request, 'books/edit_book.html', {
        'book': book,
        'form': form,
    })


def create_book(request):
    form_class = BookForm
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid:
            book = form.save(commit=False)
            book.user = request.user
            book.slug = slugify(book.name)
            book.save()
            return redirect('book_detail', slug=book.slug)

    else:
        form = form_class()

    return render(request, 'books/create_book.html', {
        'form': form,
    })


def browse_by_name(request, initial=None):
    if initial:
        books = Book.objects.filter(
            name__istartswith=initial).order_by('name')
    else:
        books = Book.objects.all().order_by('name')

    return render(request, 'search/search.html', {
        'books': books,
        'initial': initial,
    })
