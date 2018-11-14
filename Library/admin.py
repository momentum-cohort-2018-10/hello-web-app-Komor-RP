from django.contrib import admin

# import your model
from Library.models import Book


class BookAdmin(admin.ModelAdmin):
    model = Book
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}
# register model


admin.site.register(Book, BookAdmin)
