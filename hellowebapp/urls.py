from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from Library import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
    path('books/<slug>/', views.book_detail, name="book_detail"),
    path('books/<slug>/edit', views.edit_book, name='edit_book'),
    path('accounts/', include('registration.backends.simple.urls')),
    path('admin/', admin.site.urls),
]
