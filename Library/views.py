from django.shortcuts import render, redirect
from Library.forms import BookForm, BookUploadForm
from Library.models import Book, Social, Upload
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required
from django.http import Http404
from Library.forms import ContactForm
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.core.mail import mail_admins


def index(request):
    books = Book.objects.all()
    return render(request, 'index.html', {
        'books': books
    })


def book_detail(request, slug):
    book = Book.objects.get(slug=slug)
    uploads = book.uploads.all()

    return render(request, 'books/book_detail.html', {
        'book': book,
        'uploads': uploads,
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

    mail_admins("New user account created!", "Content")
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


def contact(request):
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(request.POST)

        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            contact_email = form.cleaned_data['contact_email']
            form_content = form.cleaned_data['content']

            template = get_template('contact_template.txt')

            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            }

            content = template.render(context)

            email = EmailMessage(
                'New contact form submission',
                content,
                'Your website <asdf@example.com>',
                ['asdf@gmail.com'],
                headers={'Reply-To': contact_email}
            )
            email.send()
            return redirect('contact')

    return render(request, 'contact.html', {
        'form': form_class,
    })


def user_detail(request, username):
    username = User.objects.get(username=username)

    # filter where social_account.user is equal to user
    social_accounts = Social.objects.filter(user=username)

    return render(request, 'user_detail/user_detail.html', {
        'user': username,
        'social_accounts': social_accounts,
    })

@login_required
def edit_book_uploads(request, slug):
    book = Book.objects.get(slug=slug)

    if book.user != request.user:
        raise Http404

    form_class = BookUploadForm

    if request.method == 'POST':
        form = form_class(data=request.POST,
                          files=request.FILES,
                          instance=book)

        if form.is_valid():
            Upload.objects.create(
                image=form.cleaned_data['image'],
                book=book,
            )
            return redirect('edit_book_uploads', slug=book.slug)

    else:
        form = form_class(instance=book)
        uploads = book.uploads.all()
        return render(request, 'books/edit_book_uploads.html', {
            'book': book,
            'form': form,
            'uploads': uploads,
        })
