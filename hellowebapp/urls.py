from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView, RedirectView

from Library import views
from Library.backends import MyRegistrationView
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetCompleteView,
    PasswordResetConfirmView,
    PasswordChangeView,
    PasswordChangeDoneView,
)


urlpatterns = [
    path('', views.index, name='home'),
    path('about/',
         TemplateView.as_view(template_name='about.html'),
         name='about'),

    path('contact/',
         TemplateView.as_view(template_name='contact.html'),
         name='contact'),



    path('books/<slug>/', views.book_detail, name="book_detail"),
    path('books/<slug>/edit', views.edit_book, name='edit_book'),

    path('browse/', RedirectView.as_view(
         pattern_name='browse', permanent=True)),

    path('books/', RedirectView.as_view(
        pattern_name='browse', permanent=True)),

    path('browse/name/', views.browse_by_name, name='browse'),

    path('browse/name/<initial>/',
         views.browse_by_name,
         name="browse_by_name"),

    path('accounts/password/reset/',
         PasswordResetView.as_view(
             template_name='registration/password_reset_form.html'),
         name="password_reset"),

    path('accounts/password/reset/done',
         PasswordResetDoneView.as_view(
             template_name='registration/password_reset_done.html'),
         name="password_reset_done"),

    path('accounts/password/reset/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(
             template_name='registration/password_reset_confirm.html'),
         name="password_reset_confirm"),

    path('accounts/password/done/',
         PasswordResetCompleteView.as_view(
             template_name='registration/password_reset_complete.html'),
         name="password_reset_complete"),

    path('accounts/password/change/',
         PasswordChangeView.as_view(
             template_name="registration/password_change_form.html"),
         name="password_change"),

    path('accounts/password/change/done',
         PasswordChangeDoneView.as_view(
             template_name='registration/password_change_done.html'),
         name="password_change_done"),

    path('accounts/register/',
         MyRegistrationView.as_view(),
         name='registration_register'),

    path('accounts/create_book/',
         views.create_book,
         name='registration_create_book'),

    path('accounts/', include('registration.backends.simple.urls')),
    path('admin/', admin.site.urls),
]
