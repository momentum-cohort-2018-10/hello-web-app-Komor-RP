from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from Library import views
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

    path('accounts/', include('registration.backends.simple.urls')),
    path('admin/', admin.site.urls),
]
